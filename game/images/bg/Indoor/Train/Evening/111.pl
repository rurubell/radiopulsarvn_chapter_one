#!/usr/bin/perl


#Скрипт для обновления спрайтов (пересоздания всех персонажей)


use strict;
use warnings;
use utf8;


my @s_png_files = `ls -1 *.png`;
chomp( @s_png_files );

for( my $i = 0; $i < @s_png_files; $i++ )
{
	print( $s_png_files[ $i ] . "\n" );
	system( "./colortemp -t 5000 " . $s_png_files[ $i ] . " ./out/" . $s_png_files[ $i ] );
}
