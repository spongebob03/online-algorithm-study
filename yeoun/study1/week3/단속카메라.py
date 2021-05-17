def solution(routes):
	answer = 0
	# 도로가 있기 전의 위치로 카메라 초기화 
	camera = -30001

	# 진출 지점이 이른 순으로 정렬 
	routes.sort(key=lambda x: x[1])

	# 모든 자동차가 늦어도 진출 지점에는 꼭 촬영되도록 
	for route in routes:
		enter, exit = route 
		# 진입 전에만 카메라가 있었다면 
		if camera < enter:
			# 진출 지점에 카메라를 두어서 찍히도록 하기 
			camera = exit 
			answer += 1 
		# 진입 이후에 카메라가 있었다면 무조건 나가기 전에 찍힘
		# routes를 진출 지점이 이른 순으로 정렬했으므로 

	return answer 