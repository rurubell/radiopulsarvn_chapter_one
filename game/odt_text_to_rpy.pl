#!/usr/bin/perl


#Скрипт для перегона обычного, doc-текста в ренпайный вариант


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


#Хэш имен
my %s_names_hash = 
(
	"Касуми", "kasumi",
	"Кендзи", "kenji",
	"Айко", "aiko",
	"Ватанабэ", "watanabe",
	"Телевизор", "tv",
	"Тётка", "kasumis_aunt",
	"Телефон", "kenji_phone",
	"Крик", "someones_cry",
	"Голос", "someones_voice",
	"Мусорщик 1", "trash_man_01",
	"Мусорщик 2", "trash_man_02",
	"Мусорщик 3", "trash_man_03",
	"Мальчик", "hooligan"
);


my @s_file_lines = readUTF8FileAsStringArr( $S_FILE_PATH );


for( my $i = 0; $i < @s_file_lines; $i++ )
{
	if( length( $s_file_lines[ $i ] ) <= 0 ) 
	{
		print( "\n" );
		next;
	}
	
	$s_file_lines[ $i ] =~ s/\!\?/⁈/gi;
	$s_file_lines[ $i ] =~ s/\?\!/⁈/gi;
	$s_file_lines[ $i ] =~ s/\.\.\./…/gi;
	
	my @names_hash_keys_array = ( keys %s_names_hash );
	for( my $j = 0; $j < @names_hash_keys_array; $j++ )
	{
		#Если это диологовая строка (типа Айко: "..." Кендзи: "..." и тп)
		if( index( $s_file_lines[ $i ], $names_hash_keys_array[ $j ] . ":" ) != -1 )
		{
			$s_file_lines[ $i ] =~ s/.*?://; #Удаляем все перед :
			$s_file_lines[ $i ] =~ s/«//gi; #Удаляем кавычки
			$s_file_lines[ $i ] =~ s/»//gi;
			$s_file_lines[ $i ]=~ s/^\s+|\s+$//g; #Удаляем пробелы в начале и конце строки
			
			print( $s_names_hash{ $names_hash_keys_array[ $j ] } . " \"" . $s_file_lines[ $i ] . "\"\n" );
			
			goto double_cycle_next_met;
		}
	}
	
	my @strings = split( /(?<=[\.\!\?])\s*/, $s_file_lines[ $i ] );
	for( my $j = 0; $j < @strings; $j++ )
	{
		print( "\"" . $strings[ $j ] . "\"\n" );
	}
	
	double_cycle_next_met:
	next;
}
