class SizeExt:
    async def sizes(
            self, *,
            policy = (),

            size = None,
            width: int = None,
            height: int = None,

            min_size = None,
            min_width: int = None,
            min_height: int = None,

            max_size = None,
            max_width: int = None,
            max_height: int = None,

            fixed_size = None,
            fixed_width: int = None,
            fixed_height: int = None
    ) -> 'SizeExt':
        return self
