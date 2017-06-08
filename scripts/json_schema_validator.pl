#!/usr/bin/env perl
# Validate submission records line by line.
# Stdout: correct submission records
# Stderr: submission errors, warnings
# Usage: cat submissions-file.json | ./json_schema_validator.pl (<schema_dir>) > validated-file.json
use strict;
use JSON;
use Data::Dumper;
use JSON::Validator;
use File::Slurp;
use File::Basename;

my $dir = $ARGV[0] // ( dirname(__FILE__) . "/.." );

my $schema = $dir . "/src/base.json" ;

my $schema_version = from_json(read_file($schema))->{'version'};

my $validator = JSON::Validator->new;
$validator->schema($schema);

my $err_count  = 0;

while(<STDIN>){
   my $record = from_json($_);
   $record->{'validated_against_schema_version'} = $schema_version;

   my @errors = $validator->validate($record);

   if(@errors){
      print STDERR Dumper $_ foreach @errors;
      $err_count++;
   } else {
     print STDOUT to_json($record) ."\n" ;
   }
   if($err_count > 1000){
     die "Too many errors. Giving up";
   }
}

if($err_count>0){
   die "Exited with $err_count evidence line(s) with errors";
}
