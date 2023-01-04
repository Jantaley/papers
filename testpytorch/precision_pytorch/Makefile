SRC_DIR :=src
OBJ_DIR :=obj
BIN_DIR :=bin
IDIR    :=include
CXX := g++-10 -std=c++14 

TARGET :=$(BIN_DIR)/test
CXX_FLAGS:=-I$(IDIR) #-I$(CON_IDIR) -I$(CON_MODEL_DIR)
C_FLAGS := -I${SYSTEMC_HOME}/include -O0 -g3 -Wall -c
LD_FLAGS= -L${SYSTEMC_HOME}/lib 
LIBS := -lsystemc

C_SRC := $(wildcard $(SRC_DIR)/*.cc) 
CPP_SRC := $(wildcard $(SRC_DIR)/*.cpp)
CC_OBJS := $(patsubst $(SRC_DIR)/%.cc,$(OBJ_DIR)/%.o,$(C_SRC))
CPP_OBJS :=$(patsubst $(SRC_DIR)/%.cpp,$(OBJ_DIR)/%.o,$(CPP_SRC))
OBJS :=$(CC_OBJS) $(CPP_OBJS)

.PHONY: $(TARGET)

all:$(TARGET) 
show:
	@echo $(OBJS)	
	@echo $(CPP_SRC)
	@echo $(C_SRC)
$(TARGET): $(OBJS) | $(BIN_DIR)
	@echo 'building binary $(@F)'
	$(CXX) $(LD_FLAGS) -o $@ $(OBJS)  $(LIBS)

$(OBJ_DIR)/%.o:$(SRC_DIR)/%.cc| $(OBJ_DIR)  
	@echo 'Building file: $(@F)'
	@echo '--------------------'
	@echo 'Invoking: GNU CPP Compiler'
	$(CXX) $(CXX_FLAGS) $(C_FLAGS)  -o $@ $< 
	@echo 'Finished building: $(@F)'
	@echo ' '

$(OBJ_DIR)/%.o:$(SRC_DIR)/%.cpp | $(OBJ_DIR)  
	@echo 'Building file: $(@F)'
	@echo '--------------------'
	@echo 'Invoking: GNU CPP Compiler'
	echo $(C_FLAGS)
	$(CXX) $(CXX_FLAGS) $(C_FLAGS)  -o $@ $< 
	@echo 'Finished building: $(@F)'
	@echo ' '

$(BIN_DIR) $(OBJ_DIR):
	mkdir -p $@

run:$(TARGET)
	./$(TARGET) #> results/running.log

clean:
	@$(RM) -rv $(BIN_DIR) $(OBJ_DIR)	
-include $(OBJS:.o=.d)
