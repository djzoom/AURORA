#!/bin/zsh
# 双击启动：模拟学生课程审核流水线（学生=Haiku，教授=Sonnet，不占 Fable 5）
# 断点续传：随时 Ctrl+C 中断，下次双击自动从 progress.json + 已有日志文件继续。

export PATH="/Users/z/.nvm/versions/node/v20.19.0/bin:$PATH"
export LESSON_PARALLEL="${LESSON_PARALLEL:-4}"
cd /Users/z/AURORA || exit 1

echo "════════════════════════════════════════════"
echo " 课程审核流水线 (L01–L99)"
echo " 进度文件: docs/current/audit/sim_students/progress.json"
echo " 日志:     docs/current/audit/sim_students/run.log"
echo " 监控面板: python3 scripts/sim_students_tui.py"
echo " 中断后再次双击本文件即可断点续跑"
echo "════════════════════════════════════════════"

# caffeinate 防止系统休眠导致中断
caffeinate -dims python3 scripts/sim_students_audit.py
status=$?

echo ""
if [ $status -eq 0 ]; then
  echo "✅ 全部完成。"
elif [ $status -eq 3 ]; then
  echo "⚠ 检测到另一个课程审核实例正在运行，为避免并发写入已退出。"
else
  echo "⏸ 已暂停（多为用量限额或手动中断），进度已保存，稍后再次双击继续。"
fi
echo "按回车键关闭窗口…"
read
