module SISO(
input i,clr,clk,
output o);
 
wire [2:0] t;
 
dffwsr a(i,clk,clr,t[0]);
dffwsr b(t[0],clk,clr,t[1]);
dffwsr c(t[1],clk,clr,t[2]);
dffwsr d(t[2],clk,clr,o);
 
endmodule
 
 
module dffwsr(
input d,clk,rst,
output reg q);
 
always@(posedge clk )
begin
	if(rst) 
	begin 
	q<=0; 
	end
	else begin q<=d; end
end
 
endmodule