class Metadata:

    def get_metadata(self, items: int, pages: int, total: int) -> list:
        """
        Creates metadata for page links
        :param items: int
        :param pages: int
        :param total: int
        :return:
        """
        metadata = {'page': pages, 'per_page': items,
                    'total_count': total}
        links = self.get_link_data(items, pages, total)
        metadata = [links, metadata]
        return metadata

    def get_link_data(self, items: int, pages: int, total: int) -> dict:
        """
        Creates link data
        :param items: int
        :param pages: int
        :param total: int
        :return: dict
        """
        previous = self.get_previous_page_link(pages)
        last = round(total / items)
        next_page = self.get_next_page_link(last, pages)
        last = str(last)
        pages = str(pages)
        items = '&items=' + str(items)
        current = '/?page=' + pages + items
        first = '/?page=1' + items
        previous = '/?page=' + previous + items
        next_page = '/?page=' + next_page + items
        last = '/?page=' + last + items
        links = {'self': current, 'first': first, 'previous': previous,
                 'next': next_page, 'last': last}
        return links

    @staticmethod
    def get_previous_page_link(pages: int) -> str:
        """
        gets link address for previous page
        :param pages: int
        :return: str
        """
        if pages is 1:
            previous = '1'
        else:
            previous = str(pages - 1)
        return previous

    @staticmethod
    def get_next_page_link(last: int, pages: int) -> str:
        """
        gets link address for next page
        :param pages: int
        :param last: int
        :return: str
        """
        if last == pages:
            next_page = str(last)
        else:
            next_page = str(pages + 1)
        return next_page