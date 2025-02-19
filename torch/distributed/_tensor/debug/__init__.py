from torch.distributed._tensor.api import DTensor


def get_sharding_prop_cache_info():
    """
    Get the cache info for the sharding propagation cache, used for debugging purpose only.
    """
    return (
        DTensor._propagator.propagate_op_sharding.cache_info()  # type:ignore[attr-defined]
    )
