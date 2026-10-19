import React, { useState, useEffect } from 'react';
import { Loader2, Sparkles, Clock, CheckCircle, AlertCircle, Zap } from 'lucide-react';

export interface LoadingProgressProps {
  isVisible: boolean;
  stage: 'generating' | 'processing' | 'finalizing' | 'complete' | 'error';
  progress?: number; // 0-100
  message?: string;
  estimatedTime?: number; // 预估剩余时间（秒）
  onCancel?: () => void;
  showCancel?: boolean;
}

/**
 * LoadingProgress 组件
 * 实现生成过程的加载动画、进度提示和预估时间显示
 */
export const LoadingProgress: React.FC<LoadingProgressProps> = ({
  isVisible,
  stage,
  progress = 0,
  message,
  estimatedTime,
  onCancel,
  showCancel = false
}) => {
  const [displayProgress, setDisplayProgress] = useState(0);
  const [elapsedTime, setElapsedTime] = useState(0);

  // 平滑进度条动画
  useEffect(() => {
    if (progress !== displayProgress) {
      const duration = 500; // 动画持续时间
      const steps = 30;
      const stepValue = (progress - displayProgress) / steps;
      let currentStep = 0;

      const timer = setInterval(() => {
        currentStep++;
        setDisplayProgress(prev => {
          const newValue = prev + stepValue;
          if (currentStep >= steps) {
            clearInterval(timer);
            return progress;
          }
          return newValue;
        });
      }, duration / steps);

      return () => clearInterval(timer);
    }
  }, [progress, displayProgress]);

  // 计时器
  useEffect(() => {
    if (!isVisible || stage === 'complete' || stage === 'error') {
      setElapsedTime(0);
      return;
    }

    const timer = setInterval(() => {
      setElapsedTime(prev => prev + 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [isVisible, stage]);

  // 重置状态
  useEffect(() => {
    if (!isVisible) {
      setDisplayProgress(0);
      setElapsedTime(0);
    }
  }, [isVisible]);

  const getStageInfo = () => {
    switch (stage) {
      case 'generating':
        return {
          icon: <Sparkles size={24} className="text-purple-400 animate-pulse" />,
          title: '正在生成角色属性',
          color: 'purple',
          bgGradient: 'from-purple-500/20 to-indigo-500/20'
        };
      case 'processing':
        return {
          icon: <Zap size={24} className="text-blue-400 animate-bounce" />,
          title: '处理中',
          color: 'blue',
          bgGradient: 'from-blue-500/20 to-cyan-500/20'
        };
      case 'finalizing':
        return {
          icon: <Loader2 size={24} className="text-green-400 animate-spin" />,
          title: '即将完成',
          color: 'green',
          bgGradient: 'from-green-500/20 to-emerald-500/20'
        };
      case 'complete':
        return {
          icon: <CheckCircle size={24} className="text-green-400" />,
          title: '生成完成',
          color: 'green',
          bgGradient: 'from-green-500/20 to-emerald-500/20'
        };
      case 'error':
        return {
          icon: <AlertCircle size={24} className="text-red-400" />,
          title: '生成失败',
          color: 'red',
          bgGradient: 'from-red-500/20 to-pink-500/20'
        };
      default:
        return {
          icon: <Loader2 size={24} className="text-white/60 animate-spin" />,
          title: '处理中',
          color: 'white',
          bgGradient: 'from-white/10 to-white/5'
        };
    }
  };

  const formatTime = (seconds: number) => {
    if (seconds < 60) {
      return `${seconds}秒`;
    }
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}分${remainingSeconds}秒`;
  };

  const getProgressColor = () => {
    const stageInfo = getStageInfo();
    switch (stageInfo.color) {
      case 'purple': return 'bg-gradient-to-r from-purple-500 to-indigo-500';
      case 'blue': return 'bg-gradient-to-r from-blue-500 to-cyan-500';
      case 'green': return 'bg-gradient-to-r from-green-500 to-emerald-500';
      case 'red': return 'bg-gradient-to-r from-red-500 to-pink-500';
      default: return 'bg-gradient-to-r from-white/50 to-white/30';
    }
  };

  if (!isVisible) return null;

  const stageInfo = getStageInfo();

  return (
    <div className="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div className="w-full max-w-md">
        {/* 主要加载卡片 */}
        <div className={`glass-panel p-8 rounded-2xl relative overflow-hidden`}>
          {/* 背景渐变 */}
          <div className={`absolute inset-0 bg-gradient-to-br ${stageInfo.bgGradient} opacity-50`} />
          
          <div className="relative z-10 text-center">
            {/* 图标 */}
            <div className="w-16 h-16 mx-auto mb-6 rounded-full bg-white/10 flex items-center justify-center backdrop-blur-sm border border-white/20">
              {stageInfo.icon}
            </div>

            {/* 标题 */}
            <h3 className="text-xl font-bold text-white mb-2">
              {stageInfo.title}
            </h3>

            {/* 消息 */}
            {message && (
              <p className="text-sm text-white/70 mb-6 leading-relaxed">
                {message}
              </p>
            )}

            {/* 进度条 */}
            {stage !== 'error' && stage !== 'complete' && (
              <div className="mb-6">
                <div className="w-full h-2 bg-white/10 rounded-full overflow-hidden mb-3">
                  <div 
                    className={`h-full ${getProgressColor()} transition-all duration-500 ease-out`}
                    style={{ width: `${Math.max(displayProgress, 5)}%` }}
                  />
                </div>
                <div className="flex justify-between text-xs text-white/50">
                  <span>{Math.round(displayProgress)}%</span>
                  {estimatedTime && estimatedTime > 0 && (
                    <span>预计剩余 {formatTime(estimatedTime)}</span>
                  )}
                </div>
              </div>
            )}

            {/* 时间信息 */}
            <div className="flex items-center justify-center gap-4 text-xs text-white/40 mb-6">
              <div className="flex items-center gap-1">
                <Clock size={12} />
                <span>已用时 {formatTime(elapsedTime)}</span>
              </div>
              {stage === 'complete' && (
                <div className="flex items-center gap-1">
                  <CheckCircle size={12} />
                  <span>生成成功</span>
                </div>
              )}
            </div>

            {/* 取消按钮 */}
            {showCancel && onCancel && stage !== 'complete' && stage !== 'error' && (
              <button
                onClick={onCancel}
                className="px-4 py-2 text-sm text-white/60 hover:text-white/80 transition-colors border border-white/20 rounded-lg hover:bg-white/10"
              >
                取消生成
              </button>
            )}

            {/* 错误状态的重试按钮 */}
            {stage === 'error' && onCancel && (
              <button
                onClick={onCancel}
                className="px-6 py-2 text-sm bg-red-500/20 text-red-300 hover:bg-red-500/30 transition-colors border border-red-500/30 rounded-lg"
              >
                重试
              </button>
            )}
          </div>
        </div>

        {/* 提示信息 */}
        {stage === 'generating' && (
          <div className="mt-4 text-center">
            <p className="text-xs text-white/40 leading-relaxed">
              💡 正在分析您的描述并生成个性化角色属性<br/>
              📝 这个过程通常需要 10-30 秒，请耐心等待
            </p>
          </div>
        )}

        {stage === 'processing' && (
          <div className="mt-4 text-center">
            <p className="text-xs text-white/40 leading-relaxed">
              ⚡ 正在优化角色属性的细节<br/>
              🎭 确保角色个性的一致性和丰富性
            </p>
          </div>
        )}

        {stage === 'finalizing' && (
          <div className="mt-4 text-center">
            <p className="text-xs text-white/40 leading-relaxed">
              ✨ 正在完成最后的处理步骤<br/>
              💾 保存角色数据到系统中
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

export default LoadingProgress;