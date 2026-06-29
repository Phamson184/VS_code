erDiagram
    %% Định nghĩa các bảng sau khi phân rã
    R1_ABC {
        string A PK,FK
        string B PK,FK
        string C 
    }
    
    R2_ADE {
        string A PK
        string D FK
        string E 
    }
    
    R3_DIJ {
        string D PK
        string I 
        string J 
    }
    
    R4_BF {
        string B PK
        string F FK 
    }
    
    R5_FGH {
        string F PK
        string G 
        string H 
    }

    %% Thiết lập mối quan hệ (Foreign Keys)
    %% R1 cần A từ R2 và B từ R4
    R2_ADE ||--o{ R1_ABC : "Tham chiếu A"
    R4_BF ||--o{ R1_ABC : "Tham chiếu B"
    
    %% R2 cần D từ R3
    R3_DIJ ||--o{ R2_ADE : "Tham chiếu D"
    
    %% R4 cần F từ R5
    R5_FGH ||--o{ R4_BF : "Tham chiếu F"