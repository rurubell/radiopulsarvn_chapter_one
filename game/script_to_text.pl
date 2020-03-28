#!/usr/bin/perl


#Скрипт для перегона игрового скрипта в текст


use strict;
use warnings;
use utf8;
use Encode qw(decode encode);

binmode(STDOUT,':utf8');
binmode(STDIN,':utf8');


my $S_RPY_SCRIPT_FILE_PATH = $ARGV[ 0 ];


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


#В строке есть служебные слова?
sub isStringContainsServiceWords
{
	my $s_string = shift();
	
	#Список служебных слов, строки с которыми будут проигнорированы
	my @s_service_words_arr = 
	(
		"#",
		"label",
		"start",
		"init",
		"python",
		"image",
		"define",
		"show",
		"scene",
		"hide",
		"None",
		"return",
		"Text("
	);
	
	for( my $i = 0; $i < @s_service_words_arr; $i++ )
	{
		if( index( $s_string, $s_service_words_arr[ $i ] ) != -1 ) { return 1; }
	}
	
	return undef;
}


#В строке есть русские буквы?
sub isStringContainsRussianChars
{
	my $s_string = shift();
	
	my $s_alpha = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя";
	
	for( my $i = 0; $i < length( $s_alpha ); $i++ )
	{
		my $s_char = substr( $s_alpha, $i, 1 );
		if( index( $s_string, $s_char ) != -1 ) { return 1; }
	}
	
	return undef;
}


my @s_file_strings = readUTF8FileAsStringArr( $S_RPY_SCRIPT_FILE_PATH );

for( my $i = 0; $i < @s_file_strings; $i++ )
{
	if( index( $s_file_strings[ $i ], "\"" ) == -1 ) { next; }
	if( isStringContainsServiceWords( $s_file_strings[ $i ] ) ) { next; }
	if( !isStringContainsRussianChars( $s_file_strings[ $i ] ) ) { next; }
	$s_file_strings[ $i ] =~ s/^[^\"]*\"//; #Удаляем все до "
	$s_file_strings[ $i ] =~ s/\".*//; #Удаляем все после "
	
	print( $s_file_strings[ $i ] . " \n" );
}
