#!/usr/bin/perl

use strict;
use warnings;

use JSON;

my @files = `ls $ARGV[0]`;

foreach my $x (@files) {
	chomp($x);
	my $json_file="$ARGV[0]/$x";
	my $out_file="$json_file.csv";
	open(W,">$out_file");

	my $items = parse_json($json_file);
	my $top = $items->{ansible_facts};

	foreach my $tlist ( sort keys $top ){
		my $value = $items->{ansible_facts}->{$tlist};
		my $refv1=ref($value);
		if($refv1 eq ""){
			#print "$tlist is $value\n";
			print W "$tlist,$value\n";
		}
		
	}
	close(W);
}

exit (0);



sub parse_json{

        my $filepath = shift;
        my $json_data;
        my $ref_hash;

        open(R,"<$filepath");
        $json_data = <R>;
        close(R);
        $ref_hash = JSON->new()->decode($json_data);

        return $ref_hash;
}

