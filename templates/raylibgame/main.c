#include <raylib.h>

int main() {
	InitWindow(800, 600, "ray");
	while (!WindowShouldClose()) {
		ClearBackground(BLACK);
		// ..
		BeginDrawing();
		EndDrawing();
	}

	CloseWindow();
	return 0;
}
