# Copyright (c) 2023, Shanghai Iluvatar CoreX Semiconductor Co., Ltd.
# All Rights Reserved.
# Copyright (c) OpenMMLab. All rights reserved.
from .base_3droi_head import Base3DRoIHead
# from .bbox_heads import PartA2BboxHead
from .h3d_roi_head import H3DRoIHead
from .mask_heads import PointwiseSemanticHead, PrimitiveHead
from .part_aggregation_roi_head import PartAggregationROIHead
from .point_rcnn_roi_head import PointRCNNRoIHead
from .roi_extractors import Single3DRoIAwareExtractor, SingleRoIExtractor

__all__ = [
    'Base3DRoIHead', 'PartAggregationROIHead', 'PointwiseSemanticHead',
    'Single3DRoIAwareExtractor', 'SingleRoIExtractor',
    'H3DRoIHead', 'PrimitiveHead', 'PointRCNNRoIHead'
]

# __all__ = [
#     'Base3DRoIHead', 'PartAggregationROIHead', 'PointwiseSemanticHead',
#     'Single3DRoIAwareExtractor', 'PartA2BboxHead', 'SingleRoIExtractor',
#     'H3DRoIHead', 'PrimitiveHead', 'PointRCNNRoIHead'
# ]
