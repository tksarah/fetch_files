#!/usr/bin/env perl

if($ARGV[0] eq ""){ print "Not found the file\n"; exit 1; }

my $line;

open(R,"$ARGV[0]");
        open(W,">./roles/tksarah.fetch-files/vars/files.yml");
        print W "lists:\n";
        while (<R>){
                chomp($_);
                print W "  - { filename: '$_' }\n";
                }

        close(W);
close(R);

print "Created ./roles/tksarah.fetch-files/vars/files.yml \n";
