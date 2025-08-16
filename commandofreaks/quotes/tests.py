#commandofreaks/quotes/tests.py


from django.test import TestCase
from django.urls import reverse


class QuoteViewTests(TestCase):
    """
    コマンドーの名台詞出力テスト
    """
    
    def test_quote_view_returns_200(self) -> None:
        """
        quote_view が正常にレスポンスを返すかテスト
        """
        url = reverse("quote")  # urls.py の name="quote"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    
    def test_quote_view_uses_correct_template(self) -> None:
        """
        quote_view が正しいテンプレートを使うかテスト
        """
        url = reverse("quote")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "quotes/quote.html")
