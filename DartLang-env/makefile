# wtf is this BS, colors? ew
# do it anyway color blind
COLOUR_GREEN=\033[0;32m
COLOUR_RED=\033[0;31m
COLOUR_BLUE=\033[0;34m
END_COLOUR=\033[0m


ssh:
	vagrant ssh

status:
	echo "$(COLOUR_GREEN)List local machines status$(END_COLOUR)"
	vagrant status

gstatus:
	echo "$(COLOUR_GREEN)List global machines status$(END_COLOUR)"
	vagrant global-status

up:
	echo "$(COLOUR_GREEN)starting vagrant Machines$(END_COLOUR)"
	vagrant up

clean:
	echo "$(COLOUR_RED)cleaning the Machines$(END_COLOUR)"
	vagrant destroy
fclean: clean
	echo "$(COLOUR_RED)cleaning the Machines and files$(END_COLOUR)"
	rm -rf .vagrant

re: fclean up