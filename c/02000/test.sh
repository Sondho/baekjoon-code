#!/bin/sh
	
	##
	# test.sh
	##
	gcc -Wall -Wextra -Werror  02869.c 2> error.log
	check_error=`cat error.log`
	if [ "$check_error" = "" ]; then
		./a.out
	else
		cat error.log
	fi
	
