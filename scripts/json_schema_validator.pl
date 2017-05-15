#!/usr/bin/env perl
use strict;
use JSON;
use Data::Dumper;
use JSON::Validator;
use File::Basename;

if ($#ARGV < 0) {
    print "\nUsage: json_schema_validator.pl <file_to_validate> (<schema>)";
    exit;
}
my $json   = $ARGV[0];
my $dir = dirname(__FILE__);
my $schema = $ARGV[1] // "$dir/../src/base.json" ;

my $validator = JSON::Validator->new;
$validator->schema($schema);

my $line_count = 1;
my $err_count  = 0;

open(FILE, "<$json");

while(<FILE>){
   my($line) = $_;
   chomp($line);

   my @errors = $validator->validate(from_json($line));
   $line_count++;

   if(@errors){
      print "Validation error on evidence line $line_count : \t";
      print Dumper $_ foreach @errors;
      $err_count++;
   } else {
     print "\r Successfully validated line $line_count ..."

   }
   if($err_count > 1000){
     die "Too many errors. Giving up"
   }
}

if($err_count>0){
   die "Exited with $err_count evidence line(s) with errors of the total $line_count\n";
}
else {
   print "\n$line_count evidence PASSED schema validation!\n";
}
