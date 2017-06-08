#!/usr/bin/env perl
use strict;
use JSON;
use Data::Dumper;
use JSON::Validator;
use File::Slurp;

if ($#ARGV < 0) {
    die "\nUsage: cat lines | json_schema_validator.pl <schema_dir> ";
}
my $schema = $ARGV[0] . "/src/base.json" ;

my $schema_version = from_json(read_file($schema))->{'version'};

my $validator = JSON::Validator->new;
$validator->schema($schema);

my $err_count  = 0;

while(<STDIN>){
   my $record = from_json($_);
   $record->{'validated_against_schema_version'} = $schema_version;

   my @errors = $validator->validate($record);

   if(@errors){
      print Dumper $_ foreach @errors;
      $err_count++;
   } else {
     print(to_json($record), "\n");
   }
   if($err_count > 1000){
     die "Too many errors. Giving up";
   }
}

if($err_count>0){
   die "Exited with $err_count evidence line(s) with errors";
}
