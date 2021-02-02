#include <stdio.h>
#include <limits.h>

int		get_count(int N)
{
	int		min;
	int		five_count;
	int		three_count;
	int		tmp_sum;
	int		tmp_count;

	if ((N % 5 == 0) && (N % 3 == 0))
		return ((N / 5) < (N / 3) ? N / 5 : N / 3);
	min = INT_MAX;
	five_count = N / 5;
	while (five_count >= 0)
	{
		three_count = 0;
		while((tmp_sum = (5 * five_count) + (3 * three_count)) < N)
			three_count++;
		tmp_count = five_count + three_count;
		if (tmp_sum == N)
			min = tmp_count < min ? tmp_count : min;
		five_count--;
	}
	if (min == INT_MAX)
		return (-1);
	return (min);
}
int		main(void)
{
	int		N;
	
	scanf("%d", &N);
	printf("%d\n", get_count(N));
	return (0);
}
