#!/usr/bin/perl


use strict;
use warnings;
use utf8;
use List::MoreUtils qw( uniq );

use Cwd 'abs_path';


#Путь до скрипта
my $S_SELF_PATH = abs_path( $0 );
#Имя скрипта
my $S_SELF_NAME = `basename $S_SELF_PATH`;
chomp( $S_SELF_NAME );
#Путь до директории скрипта
my $S_SELF_DIR_PATH = `dirname $S_SELF_PATH`;
chomp( $S_SELF_DIR_PATH );

#Интервал между кадрами, сек
my $N_INTERVAL = 0.1;


#Узнаем имя бэка
my $s_bg_name = `basename $S_SELF_DIR_PATH`;
chomp( $s_bg_name );

#Узнаем директорию до бэка от /images/
my $n_index = index( $S_SELF_DIR_PATH, "/images/" );
my $s_images_wires_path = "." . substr( $S_SELF_DIR_PATH, $n_index ) . "/wires/";
system( "rm -f " . $s_bg_name . "_wires.rpy" );

my @arr_s_wires = `ls -1 ./wires/*.png`;
chomp( @arr_s_wires );


open( my $fh, '>', $s_bg_name . "_wires.rpy" );
print $fh "image " . $s_bg_name . "_wires:\n";

for( my $i = 0; $i < @arr_s_wires; $i++ )
{
	$n_index = rindex( $arr_s_wires[ $i ], "/" ) + 1;
	my $s_wire_path = $s_images_wires_path . substr( $arr_s_wires[ $i ], $n_index );
	
	print $fh "    \"" . $s_wire_path . "\"\n";
	print $fh "    " . $N_INTERVAL . "\n";
}

print $fh "    repeat";
