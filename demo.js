class jsonChunks {
    constructor(chunks) {
        this.chunks = chunks // 字符串数组
        this.lfBraceStack = []
        this.startChunkIndex = -1
    }
    clearChunkIndex() {
        this.startChunkIndex = -1
    }
    /**
     * 
     * @param {string} char 
     * @returns 
     */
    braceIndex(char) {
        return char.indexOf(char)
    }
    isLeftBrace(char) {
        return char === "{"
    }
    isRightBrace(char) {
        return char === "}"
    }
    /**
     * 
     * @param {string} chunk 
     */
    parseChunk(chunk) {
        this.startChunkIndex++
        let chunkSplit = chunk.split("")
        let braces = chunkSplit.filter(v => this.isLeftBrace(v) || this.isRightBrace(v))
        console.log("parse chunk", braces);
        
    }
}