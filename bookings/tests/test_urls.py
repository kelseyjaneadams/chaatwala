from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bookings.views import (
    my_bookings,
    book_table,
    edit_booking,
    delete_booking
)


class TestUrls(SimpleTestCase):
    """Test that URLs resolve to the correct views."""

    def test_my_bookings_url_resolves(self):
        """Test that the 'bookings' URL maps to the correct view."""
        url = reverse("bookings")
        self.assertEqual(resolve(url).func, my_bookings)

    def test_book_table_url_resolves(self):
        """Test that the 'book_table' URL maps to the correct view."""
        url = reverse("book_table")
        self.assertEqual(resolve(url).func, book_table)

    def test_edit_booking_url_resolves(self):
        """Test that the 'edit_booking' URL maps to the correct view."""
        url = reverse("edit_booking", args=[1])
        self.assertEqual(resolve(url).func, edit_booking)

    def test_delete_booking_url_resolves(self):
        """Test that the 'delete_booking' URL maps to the correct view."""
        url = reverse("delete_booking", args=[1])
        self.assertEqual(resolve(url).func, delete_booking)