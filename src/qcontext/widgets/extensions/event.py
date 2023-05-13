class EventExt:
    EventType = type[callable]

    async def events(
            self, *,
            on_click: EventType = None,
            on_change: EventType = None
    ) -> 'EventExt':

        return self
