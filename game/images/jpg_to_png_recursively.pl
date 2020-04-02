#!/usr/bin/perl


#Скрипт для рекурсивного конвертирования jpg в png


use strict;
use warnings;
use utf8;
use Scalar::Util qw( looks_like_number );
use Encode qw(decode encode);
use Cwd 'abs_path';
use File::Basename;
use Term::ANSIColor;

binmode(STDOUT,':utf8');
binmode(STDIN,':utf8');


my @s_files = `find . -type f`;
chomp( @s_files );

for( my $i = 0; $i < @s_files; $i++ )
{
	if( index( $s_files[ $i ], ".jpg" ) != -1 )
	{
		print $s_files[ $i ] . "\n";
		
		my $png_file_path = $s_files[ $i ];
		$png_file_path =~ s{\.[^.]+$}{};
		$png_file_path .= ".png";
		
		system( "convert " . $s_files[ $i ] . " " . $png_file_path );
		system( "rm " . $s_files[ $i ] );
	}
	
	#Замена всех ".jpg" на ".png в .rpy файлах
	if( ( index( $s_files[ $i ], ".rpy" ) != -1 ) and ( index( $s_files[ $i ], ".rpyc" ) == -1 ) )
	{
		print( $s_files[ $i ] . "\n" );
		system( "sed -i 's/\.jpg/\.png/g' " . $s_files[ $i ] );
	}
}
