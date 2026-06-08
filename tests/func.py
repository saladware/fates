"""Test helper functions."""

from __future__ import annotations

from fates import Err, Ok, Result


def sum_non_empty(nums: list[int]) -> Result[int, str]:
    """Summarize non empty list of integers."""
    if len(nums) > 0:
        return Ok(sum(nums))
    return Err("empty")


async def async_sum_non_empty(nums: list[int]) -> Result[int, str]:
    """Async version of sum_non_empty."""
    if len(nums) > 0:
        return Ok(sum(nums))
    return Err("empty")


async def async_sum(nums: list[int]) -> int:
    """Async version of sum."""
    return sum(nums)
