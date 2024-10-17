from pydantic import BaseModel
import requests
from typing import Tuple, Optional
from .config import (
    URL_METHOD_REQUEST_VIEW,
    URL_METHOD_REQUEST_RESULT,
    URL_METHOD_REQUEST_LIST,
    URL_METHOD_REQUEST_CREATE,
    URL_METHOD_REQUEST_CHANGE,
)

from .models import (
    RequestInfo,
    RequestViewRequest,
    RequestViewResponse,
    RequestResultRequest,
    RequestResultResponse,
    RequestListFilter,
    RequestListRequest,
    RequestListResponse,
    RequestCreateRequest,
    RequestCreateResponse,
    RequestChangeRequest,
)


class IECP:
    """Класс для работы с API EW Основание в ЛК https://lk.iecp.ru"""

    def __init__(self, login: str, password: str):
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})
        # TODO logger

        self.auth = {'login': login, 'pass': password}

    def request_view(self, request_id: int) -> Tuple[bool, RequestViewResponse]:
        """Получение данных запроса

        Args:
            request_id (int): номер запроса

        Returns:
            Tuple[bool, RequestViewResponse]:
                     первое значение - результат положительный или нет
                     второе - полученные данные запроса
        """
        payload = RequestViewRequest(**(self.auth | {'requestId': request_id}))
        res = self.session.post(URL_METHOD_REQUEST_VIEW, data=payload.model_dump_json(by_alias=True))
        return self._process_response(res, RequestViewResponse)

    def request_result(self, request_id: int) -> Tuple[bool, RequestResultResponse]:
        """Получение результирующих доментоы по запросу

        Args:
            request_id (int): номер запроса

        Returns:
            Tuple[bool, RequestResultResponse]:
                     первое значение - результат положительный или нет
                     второе - полученные данные запроса

        """
        payload = RequestResultRequest(**(self.auth | {'requestId': request_id}))
        res = self.session.post(URL_METHOD_REQUEST_RESULT, data=payload.model_dump_json(by_alias=True))
        return self._process_response(res, RequestResultResponse)

    def request_list(self, filter: RequestListFilter) -> Tuple[bool, RequestListResponse]:
        """Получение списка запросов

        Args:
            filter (RequestListFilter): фильтр применяемый к списку всех запросов

        Returns:
            Tuple[bool, RequestListResponse]:
                    первое значение - результат положительный или нет
                    второе - полученные данные RequestListResponse.info
                                содержит список запросов
        """
        payload = RequestListRequest(**(self.auth | {'filter': filter}))
        res = self.session.post(
            URL_METHOD_REQUEST_LIST, data=payload.model_dump_json(by_alias=True, exclude_unset=True)
        )
        return self._process_response(res, RequestListResponse)

    def request_create(self, info: RequestInfo) -> Tuple[bool, RequestCreateResponse]:
        """Создание нового запроса

        Args:
            info (RequestInfo): данные запроса

        Returns:
            Tuple[bool, RequestCreateResponse]:
                    первое значение - результат положительный или нет
                    второе - полученные данные
                                RequestCreateResponse.requestId - номер запроса

        """
        payload = RequestCreateRequest(**(self.auth | {'info': info}))
        res = self.session.post(
            URL_METHOD_REQUEST_CREATE,
            data=payload.model_dump_json(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return self._process_response(res, RequestCreateResponse)

    def request_change(
        self, request_id: int, info: Optional[RequestInfo] = None, request_archived: bool = None
    ) -> Tuple[bool, str]:
        """Изменение данных запроса

        Args:
            request_id (int): номер запроса
            info (Optional[RequestInfo], optional): новые данные. Defaults to None.
            request_archived (bool, optional): присвоить статус архивированный.
                                    Defaults to None.

        Returns:
            Tuple[bool, str]:
                    первое значение - результат положительный или нет
                    второе - текст ошибки если есть
        """
        payload_data = {'requestId': request_id, 'requestArchived': request_archived, 'info': info}
        payload = RequestChangeRequest(**(self.auth | payload_data))
        res = self.session.post(
            URL_METHOD_REQUEST_CHANGE,
            data=payload.model_dump_json(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return self._is_response_ok_text(res)

    def _process_response(self, response: requests.Response, model: BaseModel) -> Tuple[bool, BaseModel]:
        """Обработка данных запроса, возвращает успешность запроса и модель ответа

        Args:
            response (requests.Response): ответ сервера
            model (BaseModel): модель для разбора json ответа

        Returns:
            Tuple[bool, BaseModel]:
                    первое значение - результат положительный или нет
                    второе - модель, возвращаемая при успешном ответе
        """

        if self._is_response_ok(response):
            return True, model.model_validate_json(response.text)
        else:
            if response.text:
                return False, response.text
            else:
                response.raise_for_status()

    def _is_response_ok_text(self, response: requests.Response) -> Tuple[bool, str]:
        """Обработка данных запроса, возвращает успешность запроса и текст ответа

        Args:
            response (requests.Response): ответ сервера

        Returns:
            Tuple[bool, str]:
                    первое значение - результат положительный или нет
                    второе - текстовое значение ответа сервера
        """

        if self._is_response_ok(response):
            return True, response.text
        else:
            if response.text:
                return False, response.text
            else:
                response.raise_for_status()

    def _is_response_ok(self, response: requests.Response) -> bool:
        """Проверка ответа сервена на ошибку 200

        Args:
            response (requests.Response): ответ сервера

        Returns:
            bool: True если код ответа 200, иначе False
        """
        return True if response.status_code == 200 else False


if __name__ == '__main__':
    pass
