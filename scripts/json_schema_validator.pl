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
my $err_count = 0;
open(FILE, "<$json");

while(<FILE>){
   my($line) = $_;
   chomp($line);

   my @errors = $validator->validate(from_json($line));

   if(@errors){
      warn "Error on line $line_count : \t";
      warn Dumper $_ foreach @errors;
      $err_count++;	
   }
   $line_count++;
}
if($err_count>0){
   die "Exited with $err_count errors"
}
