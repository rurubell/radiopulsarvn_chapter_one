#!/usr/bin/perl


#Скрипт для вырезания высоких частот из аудио-файла (эффект погружения под воду)


use strict;
use warnings;
use utf8;
use Encode qw(decode encode);

binmode(STDOUT,':utf8');
binmode(STDIN,':utf8');

my $S_IN_FILE_PATH = $ARGV[ 0 ];

my $s_out_file_path = $S_IN_FILE_PATH;
$s_out_file_path =~ s{\.[^.]+$}{};
$s_out_file_path .= "_Dream.mp3";

print( $s_out_file_path . "\n" );
system( "ffmpeg -y -i " . $S_IN_FILE_PATH . " -af \"equalizer=f=3000:width_type=h:width=2000:g=-50\" " . $s_out_file_path );
