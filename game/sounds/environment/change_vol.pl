#!/usr/bin/perl


#Скрипт для увеличения/уменьшения громкости аудиофайлов


use strict;
use warnings;
use utf8;
use Encode qw(decode encode);

binmode(STDOUT,':utf8');
binmode(STDIN,':utf8');


my $S_VOL_LEVEL = "3.0";


system( "mkdir -p ./out" );

my @s_files = `ls -1 *.mp3`;
chomp( @s_files );
for( my $i = 0; $i < @s_files; $i++ )
{
	print( $s_files[ $i ] , "\n" );
	system( "ffmpeg -y -i " . $s_files[ $i ] . " -filter:a \"volume=" . $S_VOL_LEVEL . "\" ./out/" .  $s_files[ $i ] );
}
