// 在浏览器控制台中运行这个脚本来检查前端状态

console.log("=== Fay前端状态检查 ===");

// 检查Vue实例
if (typeof app !== 'undefined') {
    console.log("✅ Vue实例存在");
    console.log("当前模式:", app.pure_mode_enabled ? "纯净AI助手" : "数字人角色");
    console.log("pure_mode_enabled值:", app.pure_mode_enabled);
    console.log("liveState值:", app.liveState);
} else {
    console.log("❌ Vue实例不存在");
}

// 检查切换按钮是否存在
const pureButton = document.querySelector('.inputmessage_pure_mode');
if (pureButton) {
    console.log("✅ 切换按钮存在");
    console.log("按钮可见性:", pureButton.style.display !== 'none' ? "可见" : "隐藏");
} else {
    console.log("❌ 切换按钮不存在");
}

// 检查CSS样式
const inputMessage = document.querySelector('.inputmessage');
if (inputMessage) {
    console.log("✅ 输入区域存在");
    console.log("输入区域宽度:", inputMessage.offsetWidth);
} else {
    console.log("❌ 输入区域不存在");
}

// 测试切换功能
console.log("\n=== 测试切换功能 ===");
if (typeof app !== 'undefined' && app.togglePureMode) {
    console.log("togglePureMode方法存在，可以手动测试:");
    console.log("运行: app.togglePureMode()");
} else {
    console.log("❌ togglePureMode方法不存在");
}

// 测试发送消息功能
console.log("\n=== 测试发送功能 ===");
if (typeof app !== 'undefined' && app.sendMessage) {
    console.log("sendMessage方法存在");
    console.log("可以手动测试发送:");
    console.log("1. app.newMessage = '测试消息'");
    console.log("2. app.sendMessage()");
} else {
    console.log("❌ sendMessage方法不存在");
}

console.log("\n=== 检查完成 ===");
console.log("请将上述信息截图发送给开发者");