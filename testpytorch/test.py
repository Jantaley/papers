import torch
import torchvision
a = torch.rand(1,9,12, 16)
b = torch.rand(1, 5)
a[:,::2] = a[:,::2] + 3
b[:,::2] = b[:,::2] + 4
k = 3
sp_s =1
sm_r = -1
m = torchvision.ops.ps_roi_align(a,b,k,sp_s,sm_r)
print(a.stride(0))
#m = torchvision.ops.MultiScaleRoIAlign(['feat1', 'feat3'], 3, 2)
#i = OrderedDict()
#i['feat1'] = torch.rand(1, 5, 64, 64)
#i['feat2'] = torch.rand(1, 5, 32, 32)  # this feature won't be used in the pooling
#i['feat3'] = torch.rand(1, 5, 16, 16)
## create some random bounding boxes
#boxes = torch.rand(6, 4) * 256; boxes[:, 2:] += boxes[:, :2]
## original image size, before computing the feature maps
#image_sizes = [(512, 512)]
#output = m(i, [boxes], image_sizes)
#print(output.shape)
#torch.Size([6, 5, 3, 3])


#def _box_inter_union(boxes1: Tensor, boxes2: Tensor) -> Tuple[Tensor, Tensor]:
#    area1 = box_area(boxes1)
#    area2 = box_area(boxes2)
#    lt = torch.max(boxes1[:, None, :2], boxes2[:, :2])  # [N,M,2]
#    rb = torch.min(boxes1[:, None, 2:], boxes2[:, 2:])  # [N,M,2]
#    wh = _upcast(rb - lt).clamp(min=0)  # [N,M,2]
#    inter = wh[:, :, 0] * wh[:, :, 1]  # [N,M]
#    union = area1[:, None] + area2 - inter
#    return inter, union

