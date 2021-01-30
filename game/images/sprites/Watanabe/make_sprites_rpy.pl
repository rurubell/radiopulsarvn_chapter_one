#!/usr/bin/perl


#Скрипт для создания .rpy файлов спрайтов персонажа


use strict;
use warnings;
use utf8;


my $s_path_prefix = "images/sprites/"; #Путь до папки со всеми спрайтами
my $s_home_dir = `basename \$PWD`; #Родительская директория
chomp( $s_home_dir );

$s_path_prefix .= $s_home_dir . "/";

my @sprite_dirs = `ls -d */ | cut -f1 -d'/'`;
chomp( @sprite_dirs );


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



#Функция чтения конфиг-файла
sub myConfFileReader
{
	my $s_file_path = shift();
	my @s_conf_lines = readUTF8FileAsStringArr( $s_file_path );
	
	my %conf_hash = ();
	
	for( my $i = 0; $i < @s_conf_lines; $i++ )
	{
		if( index( $s_conf_lines[ $i ], "#" ) != -1 ) { next; } #Комментарии пропускаем
		if( index( $s_conf_lines[ $i ], "=" ) == -1 ) { next; }
		
		my $n_index = index(  $s_conf_lines[ $i ], "=" );
		
		my $s_key = $s_conf_lines[ $i ];
		$s_key = substr( $s_conf_lines[ $i ], 0, $n_index ); #Удаляем все после "="
		$s_key =~ s/^\s+|\s+$//g; #Удалить пробелы в конце и начале строки
		$s_key =~ s/^\t+|\t+$//g; #Удалить табы в конце и начале строки
		
		my $s_value = $s_conf_lines[ $i ];
		$s_value = substr( $s_conf_lines[ $i ], $n_index + 1 ); #Удаляем все до "="
		$s_value =~ s/^\s+|\s+$//g; #Удалить пробелы в конце и начале строки
		$s_value =~ s/^\t+|\t+$//g; #Удалить табы в конце и начале строки
		$s_value =~ s/;+$//; #Удаляем ";" в конце строки 
		
		$conf_hash{ $s_key } = $s_value;
	}
	
	return %conf_hash;
}

my %conf_hash = myConfFileReader( "params.conf" );


for( my $i = 0; $i < @sprite_dirs; $i++ )
{
	if( $i != 0 ) { print( "\n\n" ); }
	
	my $s_sprite_group_name = $sprite_dirs[ $i ];
	
	my @s_sprite_images = `basename -a $sprite_dirs[ $i ]/*.png`; #Массив - имен png файлов
	chomp( @s_sprite_images );
	
	my @s_sprites_names = (); #Массив имен спрайтов (без .png)
	my @s_sprites_attributes = (); #Массив аттрибутов спрайта
	
	my $s_png_file_path = $s_sprite_group_name . "/" . $s_sprite_images[ 0 ];
	my $n_sprite_height = `identify -ping -format "%h" $s_png_file_path`; #Высота спрайта
	my $n_sprite_width = `identify -ping -format "%w" $s_png_file_path`; #Ширина спрайта
	
	#Новая высота и ширина спрайта
	my $n_new_sprite_height = $conf_hash{ "new_normal_height" };
	my $n_new_sprite_width = int( $n_sprite_width * ( $n_new_sprite_height / $n_sprite_height ) );
	
	for( my $j = 0; $j < @s_sprite_images; $j++ )
	{
		my $s_sprite_attribute = $s_sprite_images[ $j ];
		$s_sprite_attribute =~ s/\.png//gi; #Удаляем .png
		push( @s_sprites_names, $s_sprite_attribute );
		$s_sprite_attribute =~ s/$s_sprite_group_name\_//gi;
		push( @s_sprites_attributes, $s_sprite_attribute );
	}
	
	print( "#" . $s_sprite_group_name . "\n" );
	#Печатаем image xxx = ""...
	for( my $j = 0; $j < @s_sprite_images; $j++ )
	{
		print( "image " . $s_sprites_names[ $j ] . " = im.Scale( \"" . $s_path_prefix . $s_sprite_group_name . "/" . $s_sprite_images[ $j ] . "\", " . $n_new_sprite_width . ", " . $n_new_sprite_height ." )\n" );
	}
	print( "\n" );
	
	print( "layeredimage " . $s_sprite_group_name . ":\n" );
	print( "    group emotion:\n" );
	
	for( my $j = 0; $j < @s_sprite_images; $j++ )
	{
		print( "        attribute " . $s_sprites_attributes[ $j ] . ":\n" );
		print( "            \"" . $s_sprites_names[ $j ] . "\"\n" );
	}
}
