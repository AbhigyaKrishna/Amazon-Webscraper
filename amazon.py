from requests import Session, Response


class AccessException(Exception):
    pass


def _check_access(response: Response):
    if response.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in response.text:
            raise AccessException("Page was blocked by Amazon. Please try using better proxies")
        else:
            raise AccessException(f"Page must have been blocked by Amazon as the status code was {response.status_code}")


class AmazonSession(Session):
    def __init__(self):
        super().__init__()
        self.headers.update({
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/83.0.4103.61 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                      'application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.amazon.com/',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        })

        methods = ["get", "post", "put", "delete", "head", "options", "patch"]
        for method in methods:
            setattr(self, method, self._wrap(method))

    def __exit__(self, *args):
        self.close()

    def home(self) -> Response:
        r = self.get('https://www.amazon.in/')
        _check_access(r)
        return r

    def search(self, inp: str) -> Response:
        r = self.get(f'https://www.amazon.in/s?k={inp}')
        _check_access(r)
        return r

    def _wrap(self, method):
        def inner(url, **kwargs):
            r = super().request(method, url, **kwargs)
            _check_access(r)
            return r
        return inner
