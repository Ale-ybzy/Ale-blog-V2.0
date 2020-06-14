// 时间转换函数，存储在数组
function secondToDate(second) {
	if (!second) {
		return 0;
	}
	var time = new Array(0, 0, 0, 0, 0);
	if (second >= 365 * 24 * 3600) {
		time[0] = parseInt(second / (365 * 24 * 3600));
		second %= 365 * 24 * 3600;
	}
	if (second >= 24 * 3600) {
		time[1] = parseInt(second / (24 * 3600));
		second %= 24 * 3600;
	}
	if (second >= 3600) {
		time[2] = parseInt(second / 3600);
		second %= 3600;
	}
	if (second >= 60) {
		time[3] = parseInt(second / 60);
		second %= 60;
	}
	if (second > 0) {
		time[4] = second;
	}
	return time;
}
// 计算并格式化时间样式
function setTime() {
	var create_time = Math.round(new Date(Date.UTC(2018, 6, 20, 14, 0, 0)).getTime() / 1000);  //这里设置建站时间
	var timestamp = Math.round((new Date().getTime() + 8 * 60 * 60 * 1000) / 1000);  // 当前建站时间
	currentTime = secondToDate((timestamp - create_time));  // 运行时长
	currentTimeHtml = currentTime[0] + '年' + currentTime[1] + '天'
			+ currentTime[2] + '时' + currentTime[3] + '分' + currentTime[4]
			+ '秒';
	document.getElementById("htmer_time").innerHTML = currentTimeHtml;
}
setInterval(setTime, 1000);  //每秒调用一次setTime函数

# 音乐播放器

