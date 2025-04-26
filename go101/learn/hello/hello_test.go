package hello

import "testing"

func TestHello(t *testing.T) {
	t.Run("hello to someone", func(t *testing.T) {
		got := Hello("foo")
		want := "Hello, foo"

		assertStr(t, got, want)
	})

	t.Run("hello defaults", func(t *testing.T) {
		got := Hello("")
		want := "Hello, world"
		assertStr(t, got, want)

	})
}

func assertStr(t testing.TB, got, want string) {
	t.Helper()
	if got != want {
		t.Errorf("got %q want %q", got, want)
	}
}
