tf32/int8 		   	y = pooling(tf32/int8 x, pooltype, kernel_h, kernel_w, stride_h, stride_w, pad_h, pad_w, global_pooling, roundmode);
tf32/fp32/int8     	y = eltwise(tf32/fp32/int8 x, op_type, coeff);  
tf32/int8			y = innerproduct(tf32/int8 x, w, b, num_output, transpose, bias_term, axis);
tf32/fp32			y = softmax(tf32/fp32 x, axis );
tf32/fp32			y = proposal(tf32/fp32 x, bbox, delta, im_info, feat_stride, base_size, min_size, ratio, pre_nms_topn, post_nms_topn)

1.2 Pooling
1.3 Eltwise
1.4 InnerProduct 
1.5 Softmax
1.6 ReLU/LeakyReLU/RReLU 
1.7 Proposal
1.8 BatchNorm
1.9 ROIPooling
1.10 AbsVal
1.11 Bias
1.12 BNLL
1.13 Crop
1.14 Power
1.15 TanH
1.16 Reverse
1.17 Normalize 
1.18 PSROIPooling 
1.19 Permute
1.20 PRelu
1.21 PassThrough
1.22 scale
1.23 Convolution(DepthwiseConv，ConvolutionDepthwise)
1.24 Deconvolution 
1.25 ELU
1.26 Slice
1.27 Exp
1.28 Flatten
1.29 INPUT
1.30 ROIAlign
1.31 SSDDetectionOutput 
1.32 PriorBox
1.33 FSRDetectionOutput 
1.34 Reshape
1.35 Sigmoid
1.36 Concat
1.37 Upsample(darknet) 
1.38 Yolo
1.39 YoloV2DetectionOutput 
1.40 YoloV3DetectionOutput 
1.41 Log
1.42 LRN
1.43 MVN
1.44 Reduction
1.45 Split
1.46 SPP
1.47 Threshold
1.48 Tile
1.49 ShuffleChannel 
1.50 BatchedMatMul 
1.51 LSTM
1.52 ArgMax
1.53 RNN
1.54 Relu6
1.55 SpatialTransformer 
1.56 FlownetResample
1.57 DFMBPSROIAlign
1.58 RCNNProposal
1.59 RPNProposalSSD
1.60 Srelu
1.61 MDC_Correlation
1.62 DeconvolutionV1
1.63 Interp
1.64 PointPillarDecodeBox
1.65 ClassCal
1.66 PointPillarDetection
1.67 Yolov5FourInputDecodeBox
1.68 YoloNms














































































































































