import re

from utils.logger import log


class PhoneParser:
    def __init__(self, raw: str) -> None:
        self.raw = raw
        self.phone_codes = [982, 986, 912, 934]
        self.regexp = [
            re.compile(r'^\+7 (\d{3}) (\d{3}) (\d{2})(\d{2})$'),
            re.compile(r'^\+7 (\d{3}) (\d{3}) (\d{2}) (\d{2})$'),
            re.compile(r'^\+7 \((\d{3})\) (\d{3})-(\d{2})(\d{2})$'),
            re.compile(r'^\+7(\d{3})(\d{3})(\d{2})(\d{2})$'),
            re.compile(r'^8 (\d{3}) (\d{3}) (\d{2})(\d{2})$'),
            re.compile(r'^8 (\d{3}) (\d{3}) (\d{2}) (\d{2})$'),
            re.compile(r'^8 \((\d{3})\) (\d{3})-(\d{2})(\d{2})$'),
            re.compile(r'^8(\d{3})(\d{3})(\d{2})(\d{2})$'),
        ]


    def parse(self) -> str | None:
        match = self.match()
        if not match:
            log.info('could not match')
            return None

        code, *parts = match.groups()
        if int(code) not in self.phone_codes:
            log.info('did not match code')
            return None

        return f'+7-{code}-{parts[0]}-{parts[1]}{parts[2]}'


    def match(self) -> str | None:
        for pattern in self.regexp:
            match = pattern.match(self.raw)
            log.info(f'result matching: raw={self.raw} pattern={pattern}, m={match}')

            if match:
                return match

        return None
