#!/usr/bin/perl


#Скрипт для добавления пробелов в пустые строки (ориентируясь на число пробелов в начале предыдущей строки)


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


#Путь до файла
my $S_FILE_PATH = $ARGV[ 0 ];


#Get utf8 file as array of lines
sub readUTF8FileAsStringArr
{
	my $s_file_path = shift();
	open( my $file, '<:encoding( utf8 )', $s_file_path ) or die "Can't open file " . $s_file_path . "!\n";
	
	my @s_arr_of_lines = <$file>;
	chomp( @s_arr_of_lines );
	
	close( $file );
	return @s_arr_of_lines;
}


my @file_strings = readUTF8FileAsStringArr( $S_FILE_PATH );
print( $file_strings[ 0 ] . "\n" );

my $n_space_count = 0;
for( my $i = 1; $i < @file_strings; $i++ )
{
	if( length( $file_strings[ $i ] ) <= 0 ) #Если строка нулевой длинны...
	{
		my $s_result_str = "";
		for( my $j = 0; $j < $n_space_count; $j++ ) #Добавляем в нее $n_space_count пробелов
		{
			$s_result_str .= " ";
		}
		
		print( $s_result_str . "\n" );
		next;
	}
	
	$n_space_count = () = $file_strings[ $i ] =~ /\G\s/g; #Узнаем число пробелов в начале непустой строки
	print( $file_strings[ $i ] . "\n" );
}
