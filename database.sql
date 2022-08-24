CREATE TABLE blockData(                               
  blockHeight BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,                 
  previousBlockHash CHAR(64) NOT NULL,                          
  blockHash CHAR(64) NOT NULL,                       
  nonce INTEGER NOT NULL,                                    
  difficulty SMALLINT NOT NULL,                                  
  blockProducer  CHAR(64) NOT NULL                                   
);

CREATE TABLE txData(                               
  blockHeight BIGINT NOT NULL FOREIGN KEY,                 
  verifiedTx VARCHAR(65,535) NULL,                                                
);

CREATE TABLE accountData(                               
  account CHAR(64) NOT NULL PRIMARY KEY,                 
  amount INTEGER NOT NULL,                                                
);

--블록 데이터 베이스에 추가하기.
-- INSERT INTO blockData VALUES(block.blockHeight, 
                                -- block.previousBlockHash, 
                                -- block.blockHash,
                                -- block.nonce,
                                -- block.difficulty,
                                -- block.blockProducer)
-- 트랜잭션 데이터 추가하기.
-- INSERT INTO txData VALUES(block.blockHeight, block.verifiedTx[i])

-- 계정 데이터 추가하기.(사전에 트랜잭션에서 분리 작업 실행)
-- INSERT INTO accountData VALUES(acoount, amount)

-- 계정 데이터 수정하기.
-- UPDATE accountData
-- SET amount = amount
-- WHERE accountData = account