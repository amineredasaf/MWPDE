# wtf is this BS, colors? ew
# do it anyway color blind
COLOUR_GREEN=\033[0;32m
COLOUR_RED=\033[0;31m
COLOUR_BLUE=\033[0;34m
END_COLOUR=\033[0m

# INPUT_CHECK := ok

check :
ifdef INPUT_CHECK
	@echo "$(COLOUR_GREEN)• INPUT_CHECK is defined: $(INPUT_CHECK).$(END_COLOUR)"
else
	@echo "$(COLOUR_RED)• INPUT_CHECK is not defined$(END_COLOUR)"
endif


ssh:
ifdef VM
	@echo "$(COLOUR_GREEN)• Connecting to $(VM) $(END_COLOUR)"
	vagrant ssh $(VM)
else
	@echo "$(COLOUR_RED)• please provide the name of the virtual machine$(END_COLOUR)"
	@echo "► How to use: make ssh VM=yourVMname (example: dartVM)"
endif


status:
	@echo "$(COLOUR_GREEN)• List local machines status$(END_COLOUR)"
	vagrant status

gstatus:
	@echo "$(COLOUR_GREEN)• List global machines status$(END_COLOUR)"
	vagrant global-status

up-all:
	echo "$(COLOUR_GREEN)• starting vagrant Machines$(END_COLOUR)"
	@export SRC_HOME=$(SRC_HOME) && echo "PATH = $(SRC_HOME)" && vagrant up

up:
	@echo "$(COLOUR_GREEN)• starting vagrant Machines$(END_COLOUR)"
	vagrant up $(VM)

clean:
	@echo "$(COLOUR_RED)• cleaning the Machines$(END_COLOUR)"
	vagrant destroy

lsbox:
	@vagrant box list

rmbox:
ifdef BOX
	@echo "• $(BOX) will be removed"
	@vagrant box remove $(BOX)
else
	@echo "$(COLOUR_RED)• please provide the name of the box$(END_COLOUR)"
	@echo "► How to use: make rmbox BOX=yourBoxName (example: debian)"
endif

fclean: clean
	@echo "$(COLOUR_RED)• cleaning the Machines and files$(END_COLOUR)"
	rm -rf .vagrant


re: fclean up