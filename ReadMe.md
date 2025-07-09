1. 簡潔的Log
2. Page與Case邏輯獨立
3. Page包含等待頁面載入，不再透過顯性/隱性等待
4. 透過Nav()引入Module跟Page
5. 每個Case重新建立Driver，確保每次環境一致
6. Driver僅在底層呼叫，Module, Page和Case層都不會傳入Driver
7. 獨立Assertion功能