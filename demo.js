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
        let i = 0
        while (i < chunk.length) {
            console.log(chunk[i]);
            i++
        }
        
    }
}