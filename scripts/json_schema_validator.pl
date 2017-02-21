#!/usr/bin/env perl
use strict;
use JSON;
use Data::Dumper;
use JSON::Validator;

my $json   = $ARGV[0];
my $schema = $ARGV[1];

my $validator = JSON::Validator->new;
$validator->schema($schema);

my $line_count = 1;
my $err_count  = 0;

open(FILE, "<$json");

while(<FILE>){
   my($line) = $_;
   chomp($line);

   my @errors = $validator->validate(from_json($line));

   if(@errors){
      print "Validation error on evidence line $line_count : \t";
      print Dumper $_ foreach @errors;
      $err_count++;	
   }
   $line_count++;
}

if($err_count>0){
   die "Exited with $err_count evidence line(s) with errors of the total $line_count\n";
}
else {
   print "$line_count evidence PASSED schema validation!\n";
}
