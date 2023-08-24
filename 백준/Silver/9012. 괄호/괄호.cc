#include <stdio.h>
#include <string.h>

int main() {
	int n, l, r, cnt;
	char a[51];

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		cnt = 1;
		l = 0;
		r = 0;
		scanf("%s", &a);

		for (int j = 0; j < strlen(a); j++) {
			if (a[j] == '(')
				l++;
			if (a[j] == ')')
					r++;
			if (r > l) {
					cnt = 0;
					break;
			}
		}
		if (cnt == 1 && l == r)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}