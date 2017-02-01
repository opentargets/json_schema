#!/usr/bin/perl
use strict;
use JSON;
use Data::Dumper;
use JSON::Validator;

my $json   = $ARGV[0];
my $schema = $ARGV[1];

my $validator = JSON::Validator->new;
$validator->schema($schema);
my $count = 0;

open(FILE, "<$json");

while(<FILE>){
   my($line) = $_;
   chomp($line);

   my @errors = $validator->validate(from_json($line));

   if(@errors){
      print Dumper $_ foreach @errors;
    }
   else {
     $count++;
   }
}

print "$count evidence(s) PASSED schema validation !\n" if($count >0);
