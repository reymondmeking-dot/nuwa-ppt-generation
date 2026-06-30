# Speaker Notes

## slide_01_cover
开场说明：这是基于 hugohe3/ppt-master 封装后的 Hermes Skill 冒烟测试。重点展示动态 GIF 主视觉、深色科技风视觉系统，以及 PPTX 可编辑导出能力。

## slide_02_pipeline
解释流程：source 输入进入项目目录，页面以 SVG 形式生成；质量检查确保 SVG 对 PPT 兼容；导出阶段转换为原生 DrawingML PPTX。

## slide_03_motion
强调动态能力：页面中嵌入了真实 GIF 媒体，同时导出命令启用 per-element animation，使标题、图片、指标卡等组对象具备入场动画。

## slide_04_quality
说明验证不是口头描述，而是实际执行质量检查、后处理和导出命令，并检查生成的 PPTX 包结构与媒体文件。

## slide_05_close
总结：ppt-master 已作为 Hermes skill 可用，测试项目与导出文件都保留在 D:\AI\ppt-master-sparse\projects 下，可继续复用或二次生成。