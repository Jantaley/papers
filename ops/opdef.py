#concessive storage in both input and output
#reduce_sum(bool_value_vector), from host to device, set nonzero to 1
class scalarop:##one bank access from and to UB
	def minmax(a,b,mode,dtype):#dtype int64, int32, int16, int8,fp32,tf32
	def ln(self,a,dtype):#dtype int32,int8,fp32,tf32
	def exp(self,a,dtype):#dtype int32,int8,fp32,tf32
	def compare(self,a,b,mode,dtype): #condition = eq,ne,lt,gt,ge
	def breq(self,condition,pm_addr_offset):#pc=cond ? pc+1 : pc + pm_addr_offset
	def inv(self,a,dtype):#1/x, dtype int32,int8,fp32,tf32
	def inv_sqrt(self,a,dtype):#1/sqrt(x), dtype int32,int8,fp32,tf32
	def alu_expr(self,a,b,c,mode,dtype):#a+c,a*b,a*b+c,a-c,-c,a/b,a%b,abs(a), 4 modes in total,dtype int64,int32,int16,int8,fp32,tf32
	def logic_expr(self,a,b,mode,dtype):#a&b,a|b, a^b,~a,a<<b,a>>b, int8,int32
	def load(self,bank_addr,a,dtype):#dtype tf32, int8, fp32, int32, 
	def store(self,bank_addr,a,dtype):#dtype tf32, int8, fp32, int32, store scalar data shouldnot change the bits except the addr
	def dtype_converter():#dtype convert
	def set():#from tensor
	def sync_with():#wait status of a thread
	def upd_sync_status():
	def get_sync_status():
	def exit():
	def sort():#when length>128, store remains
		mark="is empty!!!"
    class one_vectorop:##one bank access from and to UB
    	def dtype_converter(self,a,b,src_dtype,dst_dtype,mask):#dtype v16tf32, v32int8, tf32, int8, fp32, int32, 
    		mark=
    	def broadcast(self,cshape,ashape,ac,a,dtype):#tf32, int8, fp32, int32,--tensor-tensor 
    	  as0,as1,as2,as3 = ashape
    	  cs0,cs1,cs2,cs3 = cshape
    	  for i in range(cs0):
    	  	ioffc = i*cs1*cs2*cs3
    	  	if(as0==1):ioffa = 0
    	  	else: ioffa = i*as1*as2*as3
    	  	for j in range(cs1):
    	  		joffc = ioffc + j*cs2*cs3
    	  		if(as1==1):joffa = ioffa + 0
    	  		else: joffa = ioffa + j*as2*as3
    	  		for k in range(cs2):
    	  			koffc = joffc + k*cs3
    	  			if(as2==1):koffa = joffa + 0
    	  			else: koffa = joffa + k*as3
    	  			for m in range(cs3):
    	  				moffc = koffc + m
    	  				if(as3==1):moffa = koffa + 0
    	  				else: moffa = koffa + m
    	  				ac[moffc]=a[moffa]
    	class segment:
    		def sum():
    			mark="is empty!!!"
    		def mean():
    			mark="is empty!!!"
    		def prod():
    			mark="is empty!!!"
    		def min():
    			mark="is empty!!!"
    		def max():
    			mark="is empty!!!"
    	def concat(,axis=0):
    		mark="is empty!!!"
    	def split(,axis=0):
    		mark="is empty!!!"
    	def roisel():
class fetch_from_ddr:#LOAD
	def simple_process():#
	def to_buffer1():
	def to_buffera():
	def to_bufferb():
	def to_bufferub():
class fetch_from_buffer1:#conv_reader
	def img2col():
	def to_buffera():
	def to_bufferb():
	def to_ub():
class fetch_from_ub:#STORE
	def col2img():
	def to_buffer1():
	def to_ddr():
	def to_bufferc():





class vectorop:	#
	mark="use 8 ports, actually it is 16 ports with inc"
	class set():
	class alu():
		def add():
			mark="is empty!!!"
		def sub():
			mark="is empty!!!"
		def mul():
			mark="is empty!!!"
		def mad():#add scalar data
			mark="is empty!!!"
		def neg():
			mark="is empty!!!"
	class nonlinear:
		def rem():
			mark="is empty!!!"
		def div():
			mark="is empty!!!"
		def inv():
			mark="is empty!!!"
		def inv_sqrt():
			mark="is empty!!!"
		def fast_exp():
		def fast_lnx():
		def fast_sincos():
		def piecewised_normails(paramlist[a0,a1..],rangelist[],):#fast alg
	class compareunit:
		def minmax(addr0,addr1,mode,step):#mode:increase, or (a,b)
			mark="is empty!!!"
		def argminmax(addr0,addr1,mode,step):
		def compare():
			mark="is empty!!!"
	class logic_expr:
		def and():
		def or():
		def xor():
		def not():
		def shl():#a<<b
		def shr():#a>>b
	class reduce():
		def minmax():
			mark="is empty!!!"
		def argminmax():
		def sum():
			mark="is empty!!!"
		def prod():
			mark="is empty!!!"
class tensorop:					
#	def img2col():
#		mark="emptyyy"
#	def conv2d():
#		mark="emptyyy"
#	def conv3d():
#		mark="emptyyy"
	def gemm():
		mark="emptyyy"
