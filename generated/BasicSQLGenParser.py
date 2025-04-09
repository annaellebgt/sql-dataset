# Generated from BasicSQLGenParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,675,189,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,1,0,1,0,1,0,1,0,1,0,1,0,3,0,37,8,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,3,0,46,8,0,1,0,3,0,49,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,80,8,0,1,1,1,1,1,1,1,1,5,1,86,8,1,
        10,1,12,1,89,9,1,3,1,91,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        5,3,102,8,3,10,3,12,3,105,9,3,1,3,1,3,1,3,3,3,110,8,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,120,8,4,1,4,1,4,1,4,5,4,125,8,4,10,4,12,
        4,128,9,4,1,5,1,5,1,5,1,5,3,5,134,8,5,1,6,1,6,1,6,5,6,139,8,6,10,
        6,12,6,142,9,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,155,
        8,9,10,9,12,9,158,9,9,3,9,160,8,9,1,10,1,10,1,10,5,10,165,8,10,10,
        10,12,10,168,9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,3,11,181,8,11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,0,1,8,15,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,2,2,0,9,9,634,634,4,0,
        10,10,16,17,33,33,82,82,199,0,79,1,0,0,0,2,90,1,0,0,0,4,92,1,0,0,
        0,6,109,1,0,0,0,8,119,1,0,0,0,10,133,1,0,0,0,12,135,1,0,0,0,14,143,
        1,0,0,0,16,146,1,0,0,0,18,159,1,0,0,0,20,161,1,0,0,0,22,180,1,0,
        0,0,24,182,1,0,0,0,26,184,1,0,0,0,28,186,1,0,0,0,30,31,5,88,0,0,
        31,32,3,18,9,0,32,33,5,64,0,0,33,36,3,2,1,0,34,35,5,103,0,0,35,37,
        3,6,3,0,36,34,1,0,0,0,36,37,1,0,0,0,37,80,1,0,0,0,38,80,1,0,0,0,
        39,40,5,88,0,0,40,41,3,18,9,0,41,42,5,64,0,0,42,45,3,2,1,0,43,44,
        5,103,0,0,44,46,3,6,3,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,
        0,47,49,3,16,8,0,48,47,1,0,0,0,48,49,1,0,0,0,49,80,1,0,0,0,50,51,
        5,88,0,0,51,52,3,18,9,0,52,53,5,64,0,0,53,54,3,2,1,0,54,55,3,10,
        5,0,55,56,3,14,7,0,56,57,3,16,8,0,57,80,1,0,0,0,58,59,5,88,0,0,59,
        60,5,56,0,0,60,61,3,18,9,0,61,62,5,64,0,0,62,63,3,2,1,0,63,64,3,
        16,8,0,64,80,1,0,0,0,65,66,5,88,0,0,66,67,3,18,9,0,67,68,5,64,0,
        0,68,69,3,2,1,0,69,70,3,10,5,0,70,71,3,14,7,0,71,72,5,88,0,0,72,
        73,3,18,9,0,73,74,5,64,0,0,74,75,3,2,1,0,75,76,5,103,0,0,76,77,3,
        6,3,0,77,78,3,16,8,0,78,80,1,0,0,0,79,30,1,0,0,0,79,38,1,0,0,0,79,
        39,1,0,0,0,79,50,1,0,0,0,79,58,1,0,0,0,79,65,1,0,0,0,80,1,1,0,0,
        0,81,91,1,0,0,0,82,87,3,4,2,0,83,84,5,6,0,0,84,86,3,4,2,0,85,83,
        1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,91,1,0,0,0,
        89,87,1,0,0,0,90,81,1,0,0,0,90,82,1,0,0,0,91,3,1,0,0,0,92,93,5,634,
        0,0,93,5,1,0,0,0,94,110,3,8,4,0,95,96,3,8,4,0,96,97,3,26,13,0,97,
        103,3,8,4,0,98,99,3,26,13,0,99,100,3,6,3,0,100,102,1,0,0,0,101,98,
        1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,110,
        1,0,0,0,105,103,1,0,0,0,106,107,3,28,14,0,107,108,3,6,3,0,108,110,
        1,0,0,0,109,94,1,0,0,0,109,95,1,0,0,0,109,106,1,0,0,0,110,7,1,0,
        0,0,111,112,6,4,-1,0,112,120,5,634,0,0,113,114,3,4,2,0,114,115,5,
        11,0,0,115,116,7,0,0,0,116,120,1,0,0,0,117,120,5,656,0,0,118,120,
        5,643,0,0,119,111,1,0,0,0,119,113,1,0,0,0,119,117,1,0,0,0,119,118,
        1,0,0,0,120,126,1,0,0,0,121,122,10,1,0,0,122,123,5,36,0,0,123,125,
        3,24,12,0,124,121,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,
        1,0,0,0,127,9,1,0,0,0,128,126,1,0,0,0,129,130,5,66,0,0,130,131,5,
        147,0,0,131,134,3,12,6,0,132,134,1,0,0,0,133,129,1,0,0,0,133,132,
        1,0,0,0,134,11,1,0,0,0,135,140,3,8,4,0,136,137,5,6,0,0,137,139,3,
        8,4,0,138,136,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,
        0,0,0,141,13,1,0,0,0,142,140,1,0,0,0,143,144,5,67,0,0,144,145,3,
        6,3,0,145,15,1,0,0,0,146,147,5,83,0,0,147,148,5,147,0,0,148,149,
        3,20,10,0,149,17,1,0,0,0,150,160,5,9,0,0,151,156,3,8,4,0,152,153,
        5,6,0,0,153,155,3,8,4,0,154,152,1,0,0,0,155,158,1,0,0,0,156,154,
        1,0,0,0,156,157,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,159,150,
        1,0,0,0,159,151,1,0,0,0,160,19,1,0,0,0,161,166,3,22,11,0,162,163,
        5,6,0,0,163,165,3,22,11,0,164,162,1,0,0,0,165,168,1,0,0,0,166,164,
        1,0,0,0,166,167,1,0,0,0,167,21,1,0,0,0,168,166,1,0,0,0,169,181,3,
        8,4,0,170,171,5,634,0,0,171,172,5,100,0,0,172,181,5,17,0,0,173,174,
        5,634,0,0,174,175,5,100,0,0,175,181,5,16,0,0,176,177,5,634,0,0,177,
        181,5,37,0,0,178,179,5,634,0,0,179,181,5,55,0,0,180,169,1,0,0,0,
        180,170,1,0,0,0,180,173,1,0,0,0,180,176,1,0,0,0,180,178,1,0,0,0,
        181,23,1,0,0,0,182,183,5,634,0,0,183,25,1,0,0,0,184,185,7,1,0,0,
        185,27,1,0,0,0,186,187,5,77,0,0,187,29,1,0,0,0,16,36,45,48,79,87,
        90,103,109,119,126,133,140,156,159,166,180
    ]

class BasicSQLGenParser ( Parser ):

    grammarFileName = "BasicSQLGenParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'$'", "'('", "')'", "'['", "']'", "','", 
                     "';'", "':'", "'*'", "'='", "'.'", "'+'", "'-'", "'/'", 
                     "'^'", "'<'", "'>'", "'<<'", "'>>'", "':='", "'<='", 
                     "'=>'", "'>='", "'..'", "'<>'", "'::'", "'%'", "<INVALID>", 
                     "<INVALID>", "'ALL'", "'ANALYSE'", "'ANALYZE'", "'AND'", 
                     "'ANY'", "'ARRAY'", "'AS'", "'ASC'", "'ASYMMETRIC'", 
                     "'BOTH'", "'CASE'", "'CAST'", "'CHECK'", "'COLLATE'", 
                     "'COLUMN'", "'CONSTRAINT'", "'CREATE'", "'CURRENT_CATALOG'", 
                     "'CURRENT_DATE'", "'CURRENT_ROLE'", "'CURRENT_TIME'", 
                     "'CURRENT_TIMESTAMP'", "'CURRENT_USER'", "'DEFAULT'", 
                     "'DEFERRABLE'", "'DESC'", "'DISTINCT'", "'DO'", "'ELSE'", 
                     "'EXCEPT'", "'FALSE'", "'FETCH'", "'FOR'", "'FOREIGN'", 
                     "'FROM'", "'GRANT'", "'GROUP'", "'HAVING'", "'IN'", 
                     "'INITIALLY'", "'INTERSECT'", "'INTO'", "'LATERAL'", 
                     "'LEADING'", "'LIMIT'", "'LOCALTIME'", "'LOCALTIMESTAMP'", 
                     "'NOT'", "'NULL'", "'OFFSET'", "'ON'", "'ONLY'", "'OR'", 
                     "'ORDER'", "'PLACING'", "'PRIMARY'", "'REFERENCES'", 
                     "'RETURNING'", "'SELECT'", "'SESSION_USER'", "'SOME'", 
                     "'SYMMETRIC'", "'TABLE'", "'THEN'", "'TO'", "'TRAILING'", 
                     "'TRUE'", "'UNION'", "'UNIQUE'", "'USER'", "'USING'", 
                     "'VARIADIC'", "'WHEN'", "'WHERE'", "'WINDOW'", "'WITH'", 
                     "'AUTHORIZATION'", "'BINARY'", "'COLLATION'", "'CONCURRENTLY'", 
                     "'CROSS'", "'CURRENT_SCHEMA'", "'FREEZE'", "'FULL'", 
                     "'ILIKE'", "'INNER'", "'IS'", "'ISNULL'", "'JOIN'", 
                     "'LEFT'", "'LIKE'", "'NATURAL'", "'NOTNULL'", "'OUTER'", 
                     "'OVER'", "'OVERLAPS'", "'RIGHT'", "'SIMILAR'", "'VERBOSE'", 
                     "'ABORT'", "'ABSOLUTE'", "'ACCESS'", "'ACTION'", "'ADD'", 
                     "'ADMIN'", "'AFTER'", "'AGGREGATE'", "'ALSO'", "'ALTER'", 
                     "'ALWAYS'", "'ASSERTION'", "'ASSIGNMENT'", "'AT'", 
                     "'ATTRIBUTE'", "'BACKWARD'", "'BEFORE'", "'BEGIN'", 
                     "'BY'", "'CACHE'", "'CALLED'", "'CASCADE'", "'CASCADED'", 
                     "'CATALOG'", "'CHAIN'", "'CHARACTERISTICS'", "'CHECKPOINT'", 
                     "'CLASS'", "'CLOSE'", "'CLUSTER'", "'COMMENT'", "'COMMENTS'", 
                     "'COMMIT'", "'COMMITTED'", "'CONFIGURATION'", "'CONNECTION'", 
                     "'CONSTRAINTS'", "'CONTENT'", "'CONTINUE'", "'CONVERSION'", 
                     "'COPY'", "'COST'", "'CSV'", "'CURSOR'", "'CYCLE'", 
                     "'DATA'", "'DATABASE'", "'DAY'", "'DEALLOCATE'", "'DECLARE'", 
                     "'DEFAULTS'", "'DEFERRED'", "'DEFINER'", "'DELETE'", 
                     "'DELIMITER'", "'DELIMITERS'", "'DICTIONARY'", "'DISABLE'", 
                     "'DISCARD'", "'DOCUMENT'", "'DOMAIN'", "'DOUBLE'", 
                     "'DROP'", "'EACH'", "'ENABLE'", "'ENCODING'", "'ENCRYPTED'", 
                     "'ENUM'", "'ESCAPE'", "'EVENT'", "'EXCLUDE'", "'EXCLUDING'", 
                     "'EXCLUSIVE'", "'EXECUTE'", "'EXPLAIN'", "'EXTENSION'", 
                     "'EXTERNAL'", "'FAMILY'", "'FIRST'", "'FOLLOWING'", 
                     "'FORCE'", "'FORWARD'", "'FUNCTION'", "'FUNCTIONS'", 
                     "'GLOBAL'", "'GRANTED'", "'HANDLER'", "'HEADER'", "'HOLD'", 
                     "'HOUR'", "'IDENTITY'", "'IF'", "'IMMEDIATE'", "'IMMUTABLE'", 
                     "'IMPLICIT'", "'INCLUDING'", "'INCREMENT'", "'INDEX'", 
                     "'INDEXES'", "'INHERIT'", "'INHERITS'", "'INLINE'", 
                     "'INSENSITIVE'", "'INSERT'", "'INSTEAD'", "'INVOKER'", 
                     "'ISOLATION'", "'KEY'", "'LABEL'", "'LANGUAGE'", "'LARGE'", 
                     "'LAST'", "'LEAKPROOF'", "'LEVEL'", "'LISTEN'", "'LOAD'", 
                     "'LOCAL'", "'LOCATION'", "'LOCK'", "'MAPPING'", "'MATCH'", 
                     "'MATCHED'", "'MATERIALIZED'", "'MAXVALUE'", "'MERGE'", 
                     "'MINUTE'", "'MINVALUE'", "'MODE'", "'MONTH'", "'MOVE'", 
                     "'NEXT'", "'NO'", "'NOTHING'", "'NOTIFY'", "'NOWAIT'", 
                     "'NULLS'", "'OBJECT'", "'OF'", "'OFF'", "'OIDS'", "'OPERATOR'", 
                     "'OPTION'", "'OPTIONS'", "'OWNED'", "'OWNER'", "'PARSER'", 
                     "'PARTIAL'", "'PARTITION'", "'PASSING'", "'PASSWORD'", 
                     "'PLANS'", "'PRECEDING'", "'PREPARE'", "'PREPARED'", 
                     "'PRESERVE'", "'PRIOR'", "'PRIVILEGES'", "'PROCEDURAL'", 
                     "'PROCEDURE'", "'PROGRAM'", "'QUOTE'", "'RANGE'", "'READ'", 
                     "'REASSIGN'", "'RECHECK'", "'RECURSIVE'", "'REF'", 
                     "'REFRESH'", "'REINDEX'", "'RELATIVE'", "'RELEASE'", 
                     "'RENAME'", "'REPEATABLE'", "'REPLACE'", "'REPLICA'", 
                     "'RESET'", "'RESTART'", "'RESTRICT'", "'RETURNS'", 
                     "'REVOKE'", "'ROLE'", "'ROLLBACK'", "'ROWS'", "'RULE'", 
                     "'SAVEPOINT'", "'SCHEMA'", "'SCROLL'", "'SEARCH'", 
                     "'SECOND'", "'SECURITY'", "'SEQUENCE'", "'SEQUENCES'", 
                     "'SERIALIZABLE'", "'SERVER'", "'SESSION'", "'SET'", 
                     "'SHARE'", "'SHOW'", "'SIMPLE'", "'SNAPSHOT'", "'STABLE'", 
                     "'STANDALONE'", "'START'", "'STATEMENT'", "'STATISTICS'", 
                     "'STDIN'", "'STDOUT'", "'STORAGE'", "'STRICT'", "'STRIP'", 
                     "'SYSID'", "'SYSTEM'", "'TABLES'", "'TABLESPACE'", 
                     "'TEMP'", "'TEMPLATE'", "'TEMPORARY'", "'TEXT'", "'TRANSACTION'", 
                     "'TRIGGER'", "'TRUNCATE'", "'TRUSTED'", "'TYPE'", "'TYPES'", 
                     "'UNBOUNDED'", "'UNCOMMITTED'", "'UNENCRYPTED'", "'UNKNOWN'", 
                     "'UNLISTEN'", "'UNLOGGED'", "'UNTIL'", "'UPDATE'", 
                     "'VACUUM'", "'VALID'", "'VALIDATE'", "'VALIDATOR'", 
                     "'VARYING'", "'VERSION'", "'VIEW'", "'VOLATILE'", "'WHITESPACE'", 
                     "'WITHOUT'", "'WORK'", "'WRAPPER'", "'WRITE'", "'XML'", 
                     "'YEAR'", "'YES'", "'ZONE'", "'BETWEEN'", "'BIGINT'", 
                     "'BIT'", "'BOOLEAN'", "'CHAR'", "'CHARACTER'", "'COALESCE'", 
                     "'DEC'", "'DECIMAL'", "'EXISTS'", "'EXTRACT'", "'FLOAT'", 
                     "'GREATEST'", "'INOUT'", "'INT'", "'INTEGER'", "'INTERVAL'", 
                     "'LEAST'", "'NATIONAL'", "'NCHAR'", "'NONE'", "'NULLIF'", 
                     "'NUMERIC'", "'OVERLAY'", "'POSITION'", "'PRECISION'", 
                     "'REAL'", "'ROW'", "'SETOF'", "'SMALLINT'", "'SUBSTRING'", 
                     "'TIME'", "'TIMESTAMP'", "'TREAT'", "'TRIM'", "'VALUES'", 
                     "'VARCHAR'", "'XMLATTRIBUTES'", "'XMLCOMMENT'", "'XMLAGG'", 
                     "'XML_IS_WELL_FORMED'", "'XML_IS_WELL_FORMED_DOCUMENT'", 
                     "'XML_IS_WELL_FORMED_CONTENT'", "'XPATH'", "'XPATH_EXISTS'", 
                     "'XMLCONCAT'", "'XMLELEMENT'", "'XMLEXISTS'", "'XMLFOREST'", 
                     "'XMLPARSE'", "'XMLPI'", "'XMLROOT'", "'XMLSERIALIZE'", 
                     "'CALL'", "'CURRENT'", "'ATTACH'", "'DETACH'", "'EXPRESSION'", 
                     "'GENERATED'", "'LOGGED'", "'STORED'", "'INCLUDE'", 
                     "'ROUTINE'", "'TRANSFORM'", "'IMPORT'", "'POLICY'", 
                     "'METHOD'", "'REFERENCING'", "'NEW'", "'OLD'", "'VALUE'", 
                     "'SUBSCRIPTION'", "'PUBLICATION'", "'OUT'", "'END'", 
                     "'ROUTINES'", "'SCHEMAS'", "'PROCEDURES'", "'INPUT'", 
                     "'SUPPORT'", "'PARALLEL'", "'SQL'", "'DEPENDS'", "'OVERRIDING'", 
                     "'CONFLICT'", "'SKIP'", "'LOCKED'", "'TIES'", "'ROLLUP'", 
                     "'CUBE'", "'GROUPING'", "'SETS'", "'TABLESAMPLE'", 
                     "'ORDINALITY'", "'XMLTABLE'", "'COLUMNS'", "'XMLNAMESPACES'", 
                     "'ROWTYPE'", "'NORMALIZED'", "'WITHIN'", "'FILTER'", 
                     "'GROUPS'", "'OTHERS'", "'NFC'", "'NFD'", "'NFKC'", 
                     "'NFKD'", "'UESCAPE'", "'VIEWS'", "'NORMALIZE'", "'DUMP'", 
                     "'PRINT_STRICT_PARAMS'", "'VARIABLE_CONFLICT'", "'ERROR'", 
                     "'USE_VARIABLE'", "'USE_COLUMN'", "'ALIAS'", "'CONSTANT'", 
                     "'PERFORM'", "'GET'", "'DIAGNOSTICS'", "'STACKED'", 
                     "'ELSIF'", "'WHILE'", "'REVERSE'", "'FOREACH'", "'SLICE'", 
                     "'EXIT'", "'RETURN'", "'QUERY'", "'RAISE'", "'SQLSTATE'", 
                     "'DEBUG'", "'LOG'", "'INFO'", "'NOTICE'", "'WARNING'", 
                     "'EXCEPTION'", "'ASSERT'", "'LOOP'", "'OPEN'", "'ABS'", 
                     "'CBRT'", "'CEIL'", "'CEILING'", "'DEGREES'", "'DIV'", 
                     "'EXP'", "'FACTORIAL'", "'FLOOR'", "'GCD'", "'LCM'", 
                     "'LN'", "'LOG10'", "'MIN_SCALE'", "'MOD'", "'PI'", 
                     "'POWER'", "'RADIANS'", "'ROUND'", "'SCALE'", "'SIGN'", 
                     "'SQRT'", "'TRIM_SCALE'", "'TRUNC'", "'WIDTH_BUCKET'", 
                     "'RANDOM'", "'SETSEED'", "'ACOS'", "'ACOSD'", "'ASIN'", 
                     "'ASIND'", "'ATAN'", "'ATAND'", "'ATAN2'", "'ATAN2D'", 
                     "'COS'", "'COSD'", "'COT'", "'COTD'", "'SIN'", "'SIND'", 
                     "'TAN'", "'TAND'", "'SINH'", "'COSH'", "'TANH'", "'ASINH'", 
                     "'ACOSH'", "'ATANH'", "'BIT_LENGTH'", "'CHAR_LENGTH'", 
                     "'CHARACTER_LENGTH'", "'LOWER'", "'OCTET_LENGTH'", 
                     "'UPPER'", "'ASCII'", "'BTRIM'", "'CHR'", "'CONCAT'", 
                     "'CONCAT_WS'", "'FORMAT'", "'INITCAP'", "'LENGTH'", 
                     "'LPAD'", "'LTRIM'", "'MD5'", "'PARSE_IDENT'", "'PG_CLIENT_ENCODING'", 
                     "'QUOTE_IDENT'", "'QUOTE_LITERAL'", "'QUOTE_NULLABLE'", 
                     "'REGEXP_COUNT'", "'REGEXP_INSTR'", "'REGEXP_LIKE'", 
                     "'REGEXP_MATCH'", "'REGEXP_MATCHES'", "'REGEXP_REPLACE'", 
                     "'REGEXP_SPLIT_TO_ARRAY'", "'REGEXP_SPLIT_TO_TABLE'", 
                     "'REGEXP_SUBSTR'", "'REPEAT'", "'RPAD'", "'RTRIM'", 
                     "'SPLIT_PART'", "'STARTS_WITH'", "'STRING_TO_ARRAY'", 
                     "'STRING_TO_TABLE'", "'STRPOS'", "'SUBSTR'", "'TO_ASCII'", 
                     "'TO_HEX'", "'TRANSLATE'", "'UNISTR'", "'AGE'", "'CLOCK_TIMESTAMP'", 
                     "'DATE_BIN'", "'DATE_PART'", "'DATE_TRUNC'", "'ISFINITE'", 
                     "'JUSTIFY_DAYS'", "'JUSTIFY_HOURS'", "'JUSTIFY_INTERVAL'", 
                     "'MAKE_DATE'", "'MAKE_INTERVAL'", "'MAKE_TIME'", "'MAKE_TIMESTAMP'", 
                     "'MAKE_TIMESTAMPTZ'", "'NOW'", "'STATEMENT_TIMESTAMP'", 
                     "'TIMEOFDAY'", "'TRANSACTION_TIMESTAMP'", "'TO_TIMESTAMP'", 
                     "'TO_CHAR'", "'TO_DATE'", "'TO_NUMBER'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\\\'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'''" ]

    symbolicNames = [ "<INVALID>", "Dollar", "OPEN_PAREN", "CLOSE_PAREN", 
                      "OPEN_BRACKET", "CLOSE_BRACKET", "COMMA", "SEMI", 
                      "COLON", "STAR", "EQUAL", "DOT", "PLUS", "MINUS", 
                      "SLASH", "CARET", "LT", "GT", "LESS_LESS", "GREATER_GREATER", 
                      "COLON_EQUALS", "LESS_EQUALS", "EQUALS_GREATER", "GREATER_EQUALS", 
                      "DOT_DOT", "NOT_EQUALS", "TYPECAST", "PERCENT", "PARAM", 
                      "Operator", "ALL", "ANALYSE", "ANALYZE", "AND", "ANY", 
                      "ARRAY", "AS", "ASC", "ASYMMETRIC", "BOTH", "CASE", 
                      "CAST", "CHECK", "COLLATE", "COLUMN", "CONSTRAINT", 
                      "CREATE", "CURRENT_CATALOG", "CURRENT_DATE", "CURRENT_ROLE", 
                      "CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER", 
                      "DEFAULT", "DEFERRABLE", "DESC", "DISTINCT", "DO", 
                      "ELSE", "EXCEPT", "FALSE_P", "FETCH", "FOR", "FOREIGN", 
                      "FROM", "GRANT", "GROUP_P", "HAVING", "IN_P", "INITIALLY", 
                      "INTERSECT", "INTO", "LATERAL_P", "LEADING", "LIMIT", 
                      "LOCALTIME", "LOCALTIMESTAMP", "NOT", "NULL_P", "OFFSET", 
                      "ON", "ONLY", "OR", "ORDER", "PLACING", "PRIMARY", 
                      "REFERENCES", "RETURNING", "SELECT", "SESSION_USER", 
                      "SOME", "SYMMETRIC", "TABLE", "THEN", "TO", "TRAILING", 
                      "TRUE_P", "UNION", "UNIQUE", "USER", "USING", "VARIADIC", 
                      "WHEN", "WHERE", "WINDOW", "WITH", "AUTHORIZATION", 
                      "BINARY", "COLLATION", "CONCURRENTLY", "CROSS", "CURRENT_SCHEMA", 
                      "FREEZE", "FULL", "ILIKE", "INNER_P", "IS", "ISNULL", 
                      "JOIN", "LEFT", "LIKE", "NATURAL", "NOTNULL", "OUTER_P", 
                      "OVER", "OVERLAPS", "RIGHT", "SIMILAR", "VERBOSE", 
                      "ABORT_P", "ABSOLUTE_P", "ACCESS", "ACTION", "ADD_P", 
                      "ADMIN", "AFTER", "AGGREGATE", "ALSO", "ALTER", "ALWAYS", 
                      "ASSERTION", "ASSIGNMENT", "AT", "ATTRIBUTE", "BACKWARD", 
                      "BEFORE", "BEGIN_P", "BY", "CACHE", "CALLED", "CASCADE", 
                      "CASCADED", "CATALOG", "CHAIN", "CHARACTERISTICS", 
                      "CHECKPOINT", "CLASS", "CLOSE", "CLUSTER", "COMMENT", 
                      "COMMENTS", "COMMIT", "COMMITTED", "CONFIGURATION", 
                      "CONNECTION", "CONSTRAINTS", "CONTENT_P", "CONTINUE_P", 
                      "CONVERSION_P", "COPY", "COST", "CSV", "CURSOR", "CYCLE", 
                      "DATA_P", "DATABASE", "DAY_P", "DEALLOCATE", "DECLARE", 
                      "DEFAULTS", "DEFERRED", "DEFINER", "DELETE_P", "DELIMITER", 
                      "DELIMITERS", "DICTIONARY", "DISABLE_P", "DISCARD", 
                      "DOCUMENT_P", "DOMAIN_P", "DOUBLE_P", "DROP", "EACH", 
                      "ENABLE_P", "ENCODING", "ENCRYPTED", "ENUM_P", "ESCAPE", 
                      "EVENT", "EXCLUDE", "EXCLUDING", "EXCLUSIVE", "EXECUTE", 
                      "EXPLAIN", "EXTENSION", "EXTERNAL", "FAMILY", "FIRST_P", 
                      "FOLLOWING", "FORCE", "FORWARD", "FUNCTION", "FUNCTIONS", 
                      "GLOBAL", "GRANTED", "HANDLER", "HEADER_P", "HOLD", 
                      "HOUR_P", "IDENTITY_P", "IF_P", "IMMEDIATE", "IMMUTABLE", 
                      "IMPLICIT_P", "INCLUDING", "INCREMENT", "INDEX", "INDEXES", 
                      "INHERIT", "INHERITS", "INLINE_P", "INSENSITIVE", 
                      "INSERT", "INSTEAD", "INVOKER", "ISOLATION", "KEY", 
                      "LABEL", "LANGUAGE", "LARGE_P", "LAST_P", "LEAKPROOF", 
                      "LEVEL", "LISTEN", "LOAD", "LOCAL", "LOCATION", "LOCK_P", 
                      "MAPPING", "MATCH", "MATCHED", "MATERIALIZED", "MAXVALUE", 
                      "MERGE", "MINUTE_P", "MINVALUE", "MODE", "MONTH_P", 
                      "MOVE", "NEXT", "NO", "NOTHING", "NOTIFY", "NOWAIT", 
                      "NULLS_P", "OBJECT_P", "OF", "OFF", "OIDS", "OPERATOR", 
                      "OPTION", "OPTIONS", "OWNED", "OWNER", "PARSER", "PARTIAL", 
                      "PARTITION", "PASSING", "PASSWORD", "PLANS", "PRECEDING", 
                      "PREPARE", "PREPARED", "PRESERVE", "PRIOR", "PRIVILEGES", 
                      "PROCEDURAL", "PROCEDURE", "PROGRAM", "QUOTE", "RANGE", 
                      "READ", "REASSIGN", "RECHECK", "RECURSIVE", "REF", 
                      "REFRESH", "REINDEX", "RELATIVE_P", "RELEASE", "RENAME", 
                      "REPEATABLE", "REPLACE", "REPLICA", "RESET", "RESTART", 
                      "RESTRICT", "RETURNS", "REVOKE", "ROLE", "ROLLBACK", 
                      "ROWS", "RULE", "SAVEPOINT", "SCHEMA", "SCROLL", "SEARCH", 
                      "SECOND_P", "SECURITY", "SEQUENCE", "SEQUENCES", "SERIALIZABLE", 
                      "SERVER", "SESSION", "SET", "SHARE", "SHOW", "SIMPLE", 
                      "SNAPSHOT", "STABLE", "STANDALONE_P", "START", "STATEMENT", 
                      "STATISTICS", "STDIN", "STDOUT", "STORAGE", "STRICT_P", 
                      "STRIP_P", "SYSID", "SYSTEM_P", "TABLES", "TABLESPACE", 
                      "TEMP", "TEMPLATE", "TEMPORARY", "TEXT_P", "TRANSACTION", 
                      "TRIGGER", "TRUNCATE", "TRUSTED", "TYPE_P", "TYPES_P", 
                      "UNBOUNDED", "UNCOMMITTED", "UNENCRYPTED", "UNKNOWN", 
                      "UNLISTEN", "UNLOGGED", "UNTIL", "UPDATE", "VACUUM", 
                      "VALID", "VALIDATE", "VALIDATOR", "VARYING", "VERSION_P", 
                      "VIEW", "VOLATILE", "WHITESPACE_P", "WITHOUT", "WORK", 
                      "WRAPPER", "WRITE", "XML_P", "YEAR_P", "YES_P", "ZONE", 
                      "BETWEEN", "BIGINT", "BIT", "BOOLEAN_P", "CHAR_P", 
                      "CHARACTER", "COALESCE", "DEC", "DECIMAL_P", "EXISTS", 
                      "EXTRACT", "FLOAT_P", "GREATEST", "INOUT", "INT_P", 
                      "INTEGER", "INTERVAL", "LEAST", "NATIONAL", "NCHAR", 
                      "NONE", "NULLIF", "NUMERIC", "OVERLAY", "POSITION", 
                      "PRECISION", "REAL", "ROW", "SETOF", "SMALLINT", "SUBSTRING", 
                      "TIME", "TIMESTAMP", "TREAT", "TRIM", "VALUES", "VARCHAR", 
                      "XMLATTRIBUTES", "XMLCOMMENT", "XMLAGG", "XML_IS_WELL_FORMED", 
                      "XML_IS_WELL_FORMED_DOCUMENT", "XML_IS_WELL_FORMED_CONTENT", 
                      "XPATH", "XPATH_EXISTS", "XMLCONCAT", "XMLELEMENT", 
                      "XMLEXISTS", "XMLFOREST", "XMLPARSE", "XMLPI", "XMLROOT", 
                      "XMLSERIALIZE", "CALL", "CURRENT_P", "ATTACH", "DETACH", 
                      "EXPRESSION", "GENERATED", "LOGGED", "STORED", "INCLUDE", 
                      "ROUTINE", "TRANSFORM", "IMPORT_P", "POLICY", "METHOD", 
                      "REFERENCING", "NEW", "OLD", "VALUE_P", "SUBSCRIPTION", 
                      "PUBLICATION", "OUT_P", "END_P", "ROUTINES", "SCHEMAS", 
                      "PROCEDURES", "INPUT_P", "SUPPORT", "PARALLEL", "SQL_P", 
                      "DEPENDS", "OVERRIDING", "CONFLICT", "SKIP_P", "LOCKED", 
                      "TIES", "ROLLUP", "CUBE", "GROUPING", "SETS", "TABLESAMPLE", 
                      "ORDINALITY", "XMLTABLE", "COLUMNS", "XMLNAMESPACES", 
                      "ROWTYPE", "NORMALIZED", "WITHIN", "FILTER", "GROUPS", 
                      "OTHERS", "NFC", "NFD", "NFKC", "NFKD", "UESCAPE", 
                      "VIEWS", "NORMALIZE", "DUMP", "PRINT_STRICT_PARAMS", 
                      "VARIABLE_CONFLICT", "ERROR", "USE_VARIABLE", "USE_COLUMN", 
                      "ALIAS", "CONSTANT", "PERFORM", "GET", "DIAGNOSTICS", 
                      "STACKED", "ELSIF", "WHILE", "REVERSE", "FOREACH", 
                      "SLICE", "EXIT", "RETURN", "QUERY", "RAISE", "SQLSTATE", 
                      "DEBUG", "LOG", "INFO", "NOTICE", "WARNING", "EXCEPTION", 
                      "ASSERT", "LOOP", "OPEN", "ABS", "CBRT", "CEIL", "CEILING", 
                      "DEGREES", "DIV", "EXP", "FACTORIAL", "FLOOR", "GCD", 
                      "LCM", "LN", "LOG10", "MIN_SCALE", "MOD", "PI", "POWER", 
                      "RADIANS", "ROUND", "SCALE", "SIGN", "SQRT", "TRIM_SCALE", 
                      "TRUNC", "WIDTH_BUCKET", "RANDOM", "SETSEED", "ACOS", 
                      "ACOSD", "ASIN", "ASIND", "ATAN", "ATAND", "ATAN2", 
                      "ATAN2D", "COS", "COSD", "COT", "COTD", "SIN", "SIND", 
                      "TAN", "TAND", "SINH", "COSH", "TANH", "ASINH", "ACOSH", 
                      "ATANH", "BIT_LENGTH", "CHAR_LENGTH", "CHARACTER_LENGTH", 
                      "LOWER", "OCTET_LENGTH", "UPPER", "ASCII", "BTRIM", 
                      "CHR", "CONCAT", "CONCAT_WS", "FORMAT", "INITCAP", 
                      "LENGTH", "LPAD", "LTRIM", "MD5", "PARSE_IDENT", "PG_CLIENT_ENCODING", 
                      "QUOTE_IDENT", "QUOTE_LITERAL", "QUOTE_NULLABLE", 
                      "REGEXP_COUNT", "REGEXP_INSTR", "REGEXP_LIKE", "REGEXP_MATCH", 
                      "REGEXP_MATCHES", "REGEXP_REPLACE", "REGEXP_SPLIT_TO_ARRAY", 
                      "REGEXP_SPLIT_TO_TABLE", "REGEXP_SUBSTR", "REPEAT", 
                      "RPAD", "RTRIM", "SPLIT_PART", "STARTS_WITH", "STRING_TO_ARRAY", 
                      "STRING_TO_TABLE", "STRPOS", "SUBSTR", "TO_ASCII", 
                      "TO_HEX", "TRANSLATE", "UNISTR", "AGE", "CLOCK_TIMESTAMP", 
                      "DATE_BIN", "DATE_PART", "DATE_TRUNC", "ISFINITE", 
                      "JUSTIFY_DAYS", "JUSTIFY_HOURS", "JUSTIFY_INTERVAL", 
                      "MAKE_DATE", "MAKE_INTERVAL", "MAKE_TIME", "MAKE_TIMESTAMP", 
                      "MAKE_TIMESTAMPTZ", "NOW", "STATEMENT_TIMESTAMP", 
                      "TIMEOFDAY", "TRANSACTION_TIMESTAMP", "TO_TIMESTAMP", 
                      "TO_CHAR", "TO_DATE", "TO_NUMBER", "Identifier", "QuotedIdentifier", 
                      "UnterminatedQuotedIdentifier", "InvalidQuotedIdentifier", 
                      "InvalidUnterminatedQuotedIdentifier", "UnicodeQuotedIdentifier", 
                      "UnterminatedUnicodeQuotedIdentifier", "InvalidUnicodeQuotedIdentifier", 
                      "InvalidUnterminatedUnicodeQuotedIdentifier", "StringConstant", 
                      "UnterminatedStringConstant", "UnicodeEscapeStringConstant", 
                      "UnterminatedUnicodeEscapeStringConstant", "BeginDollarStringConstant", 
                      "BinaryStringConstant", "UnterminatedBinaryStringConstant", 
                      "InvalidBinaryStringConstant", "InvalidUnterminatedBinaryStringConstant", 
                      "HexadecimalStringConstant", "UnterminatedHexadecimalStringConstant", 
                      "InvalidHexadecimalStringConstant", "InvalidUnterminatedHexadecimalStringConstant", 
                      "Integral", "NumericFail", "Numeric", "PLSQLVARIABLENAME", 
                      "PLSQLIDENTIFIER", "Whitespace", "Newline", "LineComment", 
                      "BlockComment", "UnterminatedBlockComment", "MetaCommand", 
                      "EndMetaCommand", "ErrorCharacter", "EscapeStringConstant", 
                      "UnterminatedEscapeStringConstant", "InvalidEscapeStringConstant", 
                      "InvalidUnterminatedEscapeStringConstant", "DollarText", 
                      "EndDollarStringConstant", "AfterEscapeStringConstantWithNewlineMode_Continued" ]

    RULE_select_statement = 0
    RULE_from_list = 1
    RULE_table_ref = 2
    RULE_c_expr = 3
    RULE_columnref = 4
    RULE_group_clause = 5
    RULE_group_by_list = 6
    RULE_having_clause = 7
    RULE_sort_clause = 8
    RULE_column_list = 9
    RULE_sortby_list = 10
    RULE_sortby = 11
    RULE_collabel = 12
    RULE_binary_op = 13
    RULE_unary_op = 14

    ruleNames =  [ "select_statement", "from_list", "table_ref", "c_expr", 
                   "columnref", "group_clause", "group_by_list", "having_clause", 
                   "sort_clause", "column_list", "sortby_list", "sortby", 
                   "collabel", "binary_op", "unary_op" ]

    EOF = Token.EOF
    Dollar=1
    OPEN_PAREN=2
    CLOSE_PAREN=3
    OPEN_BRACKET=4
    CLOSE_BRACKET=5
    COMMA=6
    SEMI=7
    COLON=8
    STAR=9
    EQUAL=10
    DOT=11
    PLUS=12
    MINUS=13
    SLASH=14
    CARET=15
    LT=16
    GT=17
    LESS_LESS=18
    GREATER_GREATER=19
    COLON_EQUALS=20
    LESS_EQUALS=21
    EQUALS_GREATER=22
    GREATER_EQUALS=23
    DOT_DOT=24
    NOT_EQUALS=25
    TYPECAST=26
    PERCENT=27
    PARAM=28
    Operator=29
    ALL=30
    ANALYSE=31
    ANALYZE=32
    AND=33
    ANY=34
    ARRAY=35
    AS=36
    ASC=37
    ASYMMETRIC=38
    BOTH=39
    CASE=40
    CAST=41
    CHECK=42
    COLLATE=43
    COLUMN=44
    CONSTRAINT=45
    CREATE=46
    CURRENT_CATALOG=47
    CURRENT_DATE=48
    CURRENT_ROLE=49
    CURRENT_TIME=50
    CURRENT_TIMESTAMP=51
    CURRENT_USER=52
    DEFAULT=53
    DEFERRABLE=54
    DESC=55
    DISTINCT=56
    DO=57
    ELSE=58
    EXCEPT=59
    FALSE_P=60
    FETCH=61
    FOR=62
    FOREIGN=63
    FROM=64
    GRANT=65
    GROUP_P=66
    HAVING=67
    IN_P=68
    INITIALLY=69
    INTERSECT=70
    INTO=71
    LATERAL_P=72
    LEADING=73
    LIMIT=74
    LOCALTIME=75
    LOCALTIMESTAMP=76
    NOT=77
    NULL_P=78
    OFFSET=79
    ON=80
    ONLY=81
    OR=82
    ORDER=83
    PLACING=84
    PRIMARY=85
    REFERENCES=86
    RETURNING=87
    SELECT=88
    SESSION_USER=89
    SOME=90
    SYMMETRIC=91
    TABLE=92
    THEN=93
    TO=94
    TRAILING=95
    TRUE_P=96
    UNION=97
    UNIQUE=98
    USER=99
    USING=100
    VARIADIC=101
    WHEN=102
    WHERE=103
    WINDOW=104
    WITH=105
    AUTHORIZATION=106
    BINARY=107
    COLLATION=108
    CONCURRENTLY=109
    CROSS=110
    CURRENT_SCHEMA=111
    FREEZE=112
    FULL=113
    ILIKE=114
    INNER_P=115
    IS=116
    ISNULL=117
    JOIN=118
    LEFT=119
    LIKE=120
    NATURAL=121
    NOTNULL=122
    OUTER_P=123
    OVER=124
    OVERLAPS=125
    RIGHT=126
    SIMILAR=127
    VERBOSE=128
    ABORT_P=129
    ABSOLUTE_P=130
    ACCESS=131
    ACTION=132
    ADD_P=133
    ADMIN=134
    AFTER=135
    AGGREGATE=136
    ALSO=137
    ALTER=138
    ALWAYS=139
    ASSERTION=140
    ASSIGNMENT=141
    AT=142
    ATTRIBUTE=143
    BACKWARD=144
    BEFORE=145
    BEGIN_P=146
    BY=147
    CACHE=148
    CALLED=149
    CASCADE=150
    CASCADED=151
    CATALOG=152
    CHAIN=153
    CHARACTERISTICS=154
    CHECKPOINT=155
    CLASS=156
    CLOSE=157
    CLUSTER=158
    COMMENT=159
    COMMENTS=160
    COMMIT=161
    COMMITTED=162
    CONFIGURATION=163
    CONNECTION=164
    CONSTRAINTS=165
    CONTENT_P=166
    CONTINUE_P=167
    CONVERSION_P=168
    COPY=169
    COST=170
    CSV=171
    CURSOR=172
    CYCLE=173
    DATA_P=174
    DATABASE=175
    DAY_P=176
    DEALLOCATE=177
    DECLARE=178
    DEFAULTS=179
    DEFERRED=180
    DEFINER=181
    DELETE_P=182
    DELIMITER=183
    DELIMITERS=184
    DICTIONARY=185
    DISABLE_P=186
    DISCARD=187
    DOCUMENT_P=188
    DOMAIN_P=189
    DOUBLE_P=190
    DROP=191
    EACH=192
    ENABLE_P=193
    ENCODING=194
    ENCRYPTED=195
    ENUM_P=196
    ESCAPE=197
    EVENT=198
    EXCLUDE=199
    EXCLUDING=200
    EXCLUSIVE=201
    EXECUTE=202
    EXPLAIN=203
    EXTENSION=204
    EXTERNAL=205
    FAMILY=206
    FIRST_P=207
    FOLLOWING=208
    FORCE=209
    FORWARD=210
    FUNCTION=211
    FUNCTIONS=212
    GLOBAL=213
    GRANTED=214
    HANDLER=215
    HEADER_P=216
    HOLD=217
    HOUR_P=218
    IDENTITY_P=219
    IF_P=220
    IMMEDIATE=221
    IMMUTABLE=222
    IMPLICIT_P=223
    INCLUDING=224
    INCREMENT=225
    INDEX=226
    INDEXES=227
    INHERIT=228
    INHERITS=229
    INLINE_P=230
    INSENSITIVE=231
    INSERT=232
    INSTEAD=233
    INVOKER=234
    ISOLATION=235
    KEY=236
    LABEL=237
    LANGUAGE=238
    LARGE_P=239
    LAST_P=240
    LEAKPROOF=241
    LEVEL=242
    LISTEN=243
    LOAD=244
    LOCAL=245
    LOCATION=246
    LOCK_P=247
    MAPPING=248
    MATCH=249
    MATCHED=250
    MATERIALIZED=251
    MAXVALUE=252
    MERGE=253
    MINUTE_P=254
    MINVALUE=255
    MODE=256
    MONTH_P=257
    MOVE=258
    NEXT=259
    NO=260
    NOTHING=261
    NOTIFY=262
    NOWAIT=263
    NULLS_P=264
    OBJECT_P=265
    OF=266
    OFF=267
    OIDS=268
    OPERATOR=269
    OPTION=270
    OPTIONS=271
    OWNED=272
    OWNER=273
    PARSER=274
    PARTIAL=275
    PARTITION=276
    PASSING=277
    PASSWORD=278
    PLANS=279
    PRECEDING=280
    PREPARE=281
    PREPARED=282
    PRESERVE=283
    PRIOR=284
    PRIVILEGES=285
    PROCEDURAL=286
    PROCEDURE=287
    PROGRAM=288
    QUOTE=289
    RANGE=290
    READ=291
    REASSIGN=292
    RECHECK=293
    RECURSIVE=294
    REF=295
    REFRESH=296
    REINDEX=297
    RELATIVE_P=298
    RELEASE=299
    RENAME=300
    REPEATABLE=301
    REPLACE=302
    REPLICA=303
    RESET=304
    RESTART=305
    RESTRICT=306
    RETURNS=307
    REVOKE=308
    ROLE=309
    ROLLBACK=310
    ROWS=311
    RULE=312
    SAVEPOINT=313
    SCHEMA=314
    SCROLL=315
    SEARCH=316
    SECOND_P=317
    SECURITY=318
    SEQUENCE=319
    SEQUENCES=320
    SERIALIZABLE=321
    SERVER=322
    SESSION=323
    SET=324
    SHARE=325
    SHOW=326
    SIMPLE=327
    SNAPSHOT=328
    STABLE=329
    STANDALONE_P=330
    START=331
    STATEMENT=332
    STATISTICS=333
    STDIN=334
    STDOUT=335
    STORAGE=336
    STRICT_P=337
    STRIP_P=338
    SYSID=339
    SYSTEM_P=340
    TABLES=341
    TABLESPACE=342
    TEMP=343
    TEMPLATE=344
    TEMPORARY=345
    TEXT_P=346
    TRANSACTION=347
    TRIGGER=348
    TRUNCATE=349
    TRUSTED=350
    TYPE_P=351
    TYPES_P=352
    UNBOUNDED=353
    UNCOMMITTED=354
    UNENCRYPTED=355
    UNKNOWN=356
    UNLISTEN=357
    UNLOGGED=358
    UNTIL=359
    UPDATE=360
    VACUUM=361
    VALID=362
    VALIDATE=363
    VALIDATOR=364
    VARYING=365
    VERSION_P=366
    VIEW=367
    VOLATILE=368
    WHITESPACE_P=369
    WITHOUT=370
    WORK=371
    WRAPPER=372
    WRITE=373
    XML_P=374
    YEAR_P=375
    YES_P=376
    ZONE=377
    BETWEEN=378
    BIGINT=379
    BIT=380
    BOOLEAN_P=381
    CHAR_P=382
    CHARACTER=383
    COALESCE=384
    DEC=385
    DECIMAL_P=386
    EXISTS=387
    EXTRACT=388
    FLOAT_P=389
    GREATEST=390
    INOUT=391
    INT_P=392
    INTEGER=393
    INTERVAL=394
    LEAST=395
    NATIONAL=396
    NCHAR=397
    NONE=398
    NULLIF=399
    NUMERIC=400
    OVERLAY=401
    POSITION=402
    PRECISION=403
    REAL=404
    ROW=405
    SETOF=406
    SMALLINT=407
    SUBSTRING=408
    TIME=409
    TIMESTAMP=410
    TREAT=411
    TRIM=412
    VALUES=413
    VARCHAR=414
    XMLATTRIBUTES=415
    XMLCOMMENT=416
    XMLAGG=417
    XML_IS_WELL_FORMED=418
    XML_IS_WELL_FORMED_DOCUMENT=419
    XML_IS_WELL_FORMED_CONTENT=420
    XPATH=421
    XPATH_EXISTS=422
    XMLCONCAT=423
    XMLELEMENT=424
    XMLEXISTS=425
    XMLFOREST=426
    XMLPARSE=427
    XMLPI=428
    XMLROOT=429
    XMLSERIALIZE=430
    CALL=431
    CURRENT_P=432
    ATTACH=433
    DETACH=434
    EXPRESSION=435
    GENERATED=436
    LOGGED=437
    STORED=438
    INCLUDE=439
    ROUTINE=440
    TRANSFORM=441
    IMPORT_P=442
    POLICY=443
    METHOD=444
    REFERENCING=445
    NEW=446
    OLD=447
    VALUE_P=448
    SUBSCRIPTION=449
    PUBLICATION=450
    OUT_P=451
    END_P=452
    ROUTINES=453
    SCHEMAS=454
    PROCEDURES=455
    INPUT_P=456
    SUPPORT=457
    PARALLEL=458
    SQL_P=459
    DEPENDS=460
    OVERRIDING=461
    CONFLICT=462
    SKIP_P=463
    LOCKED=464
    TIES=465
    ROLLUP=466
    CUBE=467
    GROUPING=468
    SETS=469
    TABLESAMPLE=470
    ORDINALITY=471
    XMLTABLE=472
    COLUMNS=473
    XMLNAMESPACES=474
    ROWTYPE=475
    NORMALIZED=476
    WITHIN=477
    FILTER=478
    GROUPS=479
    OTHERS=480
    NFC=481
    NFD=482
    NFKC=483
    NFKD=484
    UESCAPE=485
    VIEWS=486
    NORMALIZE=487
    DUMP=488
    PRINT_STRICT_PARAMS=489
    VARIABLE_CONFLICT=490
    ERROR=491
    USE_VARIABLE=492
    USE_COLUMN=493
    ALIAS=494
    CONSTANT=495
    PERFORM=496
    GET=497
    DIAGNOSTICS=498
    STACKED=499
    ELSIF=500
    WHILE=501
    REVERSE=502
    FOREACH=503
    SLICE=504
    EXIT=505
    RETURN=506
    QUERY=507
    RAISE=508
    SQLSTATE=509
    DEBUG=510
    LOG=511
    INFO=512
    NOTICE=513
    WARNING=514
    EXCEPTION=515
    ASSERT=516
    LOOP=517
    OPEN=518
    ABS=519
    CBRT=520
    CEIL=521
    CEILING=522
    DEGREES=523
    DIV=524
    EXP=525
    FACTORIAL=526
    FLOOR=527
    GCD=528
    LCM=529
    LN=530
    LOG10=531
    MIN_SCALE=532
    MOD=533
    PI=534
    POWER=535
    RADIANS=536
    ROUND=537
    SCALE=538
    SIGN=539
    SQRT=540
    TRIM_SCALE=541
    TRUNC=542
    WIDTH_BUCKET=543
    RANDOM=544
    SETSEED=545
    ACOS=546
    ACOSD=547
    ASIN=548
    ASIND=549
    ATAN=550
    ATAND=551
    ATAN2=552
    ATAN2D=553
    COS=554
    COSD=555
    COT=556
    COTD=557
    SIN=558
    SIND=559
    TAN=560
    TAND=561
    SINH=562
    COSH=563
    TANH=564
    ASINH=565
    ACOSH=566
    ATANH=567
    BIT_LENGTH=568
    CHAR_LENGTH=569
    CHARACTER_LENGTH=570
    LOWER=571
    OCTET_LENGTH=572
    UPPER=573
    ASCII=574
    BTRIM=575
    CHR=576
    CONCAT=577
    CONCAT_WS=578
    FORMAT=579
    INITCAP=580
    LENGTH=581
    LPAD=582
    LTRIM=583
    MD5=584
    PARSE_IDENT=585
    PG_CLIENT_ENCODING=586
    QUOTE_IDENT=587
    QUOTE_LITERAL=588
    QUOTE_NULLABLE=589
    REGEXP_COUNT=590
    REGEXP_INSTR=591
    REGEXP_LIKE=592
    REGEXP_MATCH=593
    REGEXP_MATCHES=594
    REGEXP_REPLACE=595
    REGEXP_SPLIT_TO_ARRAY=596
    REGEXP_SPLIT_TO_TABLE=597
    REGEXP_SUBSTR=598
    REPEAT=599
    RPAD=600
    RTRIM=601
    SPLIT_PART=602
    STARTS_WITH=603
    STRING_TO_ARRAY=604
    STRING_TO_TABLE=605
    STRPOS=606
    SUBSTR=607
    TO_ASCII=608
    TO_HEX=609
    TRANSLATE=610
    UNISTR=611
    AGE=612
    CLOCK_TIMESTAMP=613
    DATE_BIN=614
    DATE_PART=615
    DATE_TRUNC=616
    ISFINITE=617
    JUSTIFY_DAYS=618
    JUSTIFY_HOURS=619
    JUSTIFY_INTERVAL=620
    MAKE_DATE=621
    MAKE_INTERVAL=622
    MAKE_TIME=623
    MAKE_TIMESTAMP=624
    MAKE_TIMESTAMPTZ=625
    NOW=626
    STATEMENT_TIMESTAMP=627
    TIMEOFDAY=628
    TRANSACTION_TIMESTAMP=629
    TO_TIMESTAMP=630
    TO_CHAR=631
    TO_DATE=632
    TO_NUMBER=633
    Identifier=634
    QuotedIdentifier=635
    UnterminatedQuotedIdentifier=636
    InvalidQuotedIdentifier=637
    InvalidUnterminatedQuotedIdentifier=638
    UnicodeQuotedIdentifier=639
    UnterminatedUnicodeQuotedIdentifier=640
    InvalidUnicodeQuotedIdentifier=641
    InvalidUnterminatedUnicodeQuotedIdentifier=642
    StringConstant=643
    UnterminatedStringConstant=644
    UnicodeEscapeStringConstant=645
    UnterminatedUnicodeEscapeStringConstant=646
    BeginDollarStringConstant=647
    BinaryStringConstant=648
    UnterminatedBinaryStringConstant=649
    InvalidBinaryStringConstant=650
    InvalidUnterminatedBinaryStringConstant=651
    HexadecimalStringConstant=652
    UnterminatedHexadecimalStringConstant=653
    InvalidHexadecimalStringConstant=654
    InvalidUnterminatedHexadecimalStringConstant=655
    Integral=656
    NumericFail=657
    Numeric=658
    PLSQLVARIABLENAME=659
    PLSQLIDENTIFIER=660
    Whitespace=661
    Newline=662
    LineComment=663
    BlockComment=664
    UnterminatedBlockComment=665
    MetaCommand=666
    EndMetaCommand=667
    ErrorCharacter=668
    EscapeStringConstant=669
    UnterminatedEscapeStringConstant=670
    InvalidEscapeStringConstant=671
    InvalidUnterminatedEscapeStringConstant=672
    DollarText=673
    EndDollarStringConstant=674
    AfterEscapeStringConstantWithNewlineMode_Continued=675

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Select_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self, i:int=None):
            if i is None:
                return self.getTokens(BasicSQLGenParser.SELECT)
            else:
                return self.getToken(BasicSQLGenParser.SELECT, i)

        def FROM(self, i:int=None):
            if i is None:
                return self.getTokens(BasicSQLGenParser.FROM)
            else:
                return self.getToken(BasicSQLGenParser.FROM, i)

        def from_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicSQLGenParser.From_listContext)
            else:
                return self.getTypedRuleContext(BasicSQLGenParser.From_listContext,i)


        def column_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicSQLGenParser.Column_listContext)
            else:
                return self.getTypedRuleContext(BasicSQLGenParser.Column_listContext,i)


        def WHERE(self):
            return self.getToken(BasicSQLGenParser.WHERE, 0)

        def c_expr(self):
            return self.getTypedRuleContext(BasicSQLGenParser.C_exprContext,0)


        def sort_clause(self):
            return self.getTypedRuleContext(BasicSQLGenParser.Sort_clauseContext,0)


        def having_clause(self):
            return self.getTypedRuleContext(BasicSQLGenParser.Having_clauseContext,0)


        def group_clause(self):
            return self.getTypedRuleContext(BasicSQLGenParser.Group_clauseContext,0)


        def DISTINCT(self):
            return self.getToken(BasicSQLGenParser.DISTINCT, 0)

        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_select_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_statement" ):
                listener.enterSelect_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_statement" ):
                listener.exitSelect_statement(self)




    def select_statement(self):

        localctx = BasicSQLGenParser.Select_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_select_statement)
        self._la = 0 # Token type
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(BasicSQLGenParser.SELECT)

                self.state = 31
                self.column_list()
                self.state = 32
                self.match(BasicSQLGenParser.FROM)
                self.state = 33
                self.from_list()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==103:
                    self.state = 34
                    self.match(BasicSQLGenParser.WHERE)
                    self.state = 35
                    self.c_expr()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(BasicSQLGenParser.SELECT)

                self.state = 40
                self.column_list()
                self.state = 41
                self.match(BasicSQLGenParser.FROM)
                self.state = 42
                self.from_list()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==103:
                    self.state = 43
                    self.match(BasicSQLGenParser.WHERE)
                    self.state = 44
                    self.c_expr()


                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==83:
                    self.state = 47
                    self.sort_clause()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.match(BasicSQLGenParser.SELECT)
                self.state = 51
                self.column_list()
                self.state = 52
                self.match(BasicSQLGenParser.FROM)
                self.state = 53
                self.from_list()

                self.state = 54
                self.group_clause()
                self.state = 55
                self.having_clause()
                self.state = 56
                self.sort_clause()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 58
                self.match(BasicSQLGenParser.SELECT)
                self.state = 59
                self.match(BasicSQLGenParser.DISTINCT)
                self.state = 60
                self.column_list()
                self.state = 61
                self.match(BasicSQLGenParser.FROM)
                self.state = 62
                self.from_list()
                self.state = 63
                self.sort_clause()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.match(BasicSQLGenParser.SELECT)
                self.state = 66
                self.column_list()
                self.state = 67
                self.match(BasicSQLGenParser.FROM)
                self.state = 68
                self.from_list()

                self.state = 69
                self.group_clause()
                self.state = 70
                self.having_clause()
                self.state = 71
                self.match(BasicSQLGenParser.SELECT)
                self.state = 72
                self.column_list()
                self.state = 73
                self.match(BasicSQLGenParser.FROM)
                self.state = 74
                self.from_list()
                self.state = 75
                self.match(BasicSQLGenParser.WHERE)
                self.state = 76
                self.c_expr()
                self.state = 77
                self.sort_clause()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class From_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_ref(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicSQLGenParser.Table_refContext)
            else:
                return self.getTypedRuleContext(BasicSQLGenParser.Table_refContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BasicSQLGenParser.COMMA)
            else:
                return self.getToken(BasicSQLGenParser.COMMA, i)

        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_from_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom_list" ):
                listener.enterFrom_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom_list" ):
                listener.exitFrom_list(self)




    def from_list(self):

        localctx = BasicSQLGenParser.From_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_from_list)
        self._la = 0 # Token type
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1, 66, 67, 83, 103]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [634]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.table_ref()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 83
                    self.match(BasicSQLGenParser.COMMA)
                    self.state = 84
                    self.table_ref()
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_refContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(BasicSQLGenParser.Identifier, 0)

        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_table_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_ref" ):
                listener.enterTable_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_ref" ):
                listener.exitTable_ref(self)




    def table_ref(self):

        localctx = BasicSQLGenParser.Table_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_table_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(BasicSQLGenParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class C_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnref(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicSQLGenParser.ColumnrefContext)
            else:
                return self.getTypedRuleContext(BasicSQLGenParser.ColumnrefContext,i)


        def binary_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicSQLGenParser.Binary_opContext)
            else:
                return self.getTypedRuleContext(BasicSQLGenParser.Binary_opContext,i)


        def c_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicSQLGenParser.C_exprContext)
            else:
                return self.getTypedRuleContext(BasicSQLGenParser.C_exprContext,i)


        def unary_op(self):
            return self.getTypedRuleContext(BasicSQLGenParser.Unary_opContext,0)


        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_c_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterC_expr" ):
                listener.enterC_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitC_expr" ):
                listener.exitC_expr(self)




    def c_expr(self):

        localctx = BasicSQLGenParser.C_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_c_expr)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.columnref(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.columnref(0)
                self.state = 96
                self.binary_op()
                self.state = 97
                self.columnref(0)
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 98
                        self.binary_op()
                        self.state = 99
                        self.c_expr() 
                    self.state = 105
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.unary_op()
                self.state = 107
                self.c_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnrefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(BasicSQLGenParser.Identifier, 0)

        def table_ref(self):
            return self.getTypedRuleContext(BasicSQLGenParser.Table_refContext,0)


        def DOT(self):
            return self.getToken(BasicSQLGenParser.DOT, 0)

        def STAR(self):
            return self.getToken(BasicSQLGenParser.STAR, 0)

        def Integral(self):
            return self.getToken(BasicSQLGenParser.Integral, 0)

        def StringConstant(self):
            return self.getToken(BasicSQLGenParser.StringConstant, 0)

        def columnref(self):
            return self.getTypedRuleContext(BasicSQLGenParser.ColumnrefContext,0)


        def AS(self):
            return self.getToken(BasicSQLGenParser.AS, 0)

        def collabel(self):
            return self.getTypedRuleContext(BasicSQLGenParser.CollabelContext,0)


        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_columnref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnref" ):
                listener.enterColumnref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnref" ):
                listener.exitColumnref(self)



    def columnref(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BasicSQLGenParser.ColumnrefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_columnref, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 112
                self.match(BasicSQLGenParser.Identifier)
                pass

            elif la_ == 2:
                self.state = 113
                self.table_ref()

                self.state = 114
                self.match(BasicSQLGenParser.DOT)
                self.state = 115
                _la = self._input.LA(1)
                if not(_la==9 or _la==634):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                self.state = 117
                self.match(BasicSQLGenParser.Integral)
                pass

            elif la_ == 4:
                self.state = 118
                self.match(BasicSQLGenParser.StringConstant)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BasicSQLGenParser.ColumnrefContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_columnref)
                    self.state = 121
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")

                    self.state = 122
                    self.match(BasicSQLGenParser.AS)
                    self.state = 123
                    self.collabel() 
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Group_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP_P(self):
            return self.getToken(BasicSQLGenParser.GROUP_P, 0)

        def BY(self):
            return self.getToken(BasicSQLGenParser.BY, 0)

        def group_by_list(self):
            return self.getTypedRuleContext(BasicSQLGenParser.Group_by_listContext,0)


        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_group_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup_clause" ):
                listener.enterGroup_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup_clause" ):
                listener.exitGroup_clause(self)




    def group_clause(self):

        localctx = BasicSQLGenParser.Group_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_group_clause)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(BasicSQLGenParser.GROUP_P)
                self.state = 130
                self.match(BasicSQLGenParser.BY)
                self.state = 131
                self.group_by_list()
                pass
            elif token in [67]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Group_by_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnref(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicSQLGenParser.ColumnrefContext)
            else:
                return self.getTypedRuleContext(BasicSQLGenParser.ColumnrefContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BasicSQLGenParser.COMMA)
            else:
                return self.getToken(BasicSQLGenParser.COMMA, i)

        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_group_by_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup_by_list" ):
                listener.enterGroup_by_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup_by_list" ):
                listener.exitGroup_by_list(self)




    def group_by_list(self):

        localctx = BasicSQLGenParser.Group_by_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_group_by_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.columnref(0)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 136
                self.match(BasicSQLGenParser.COMMA)
                self.state = 137
                self.columnref(0)
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Having_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HAVING(self):
            return self.getToken(BasicSQLGenParser.HAVING, 0)

        def c_expr(self):
            return self.getTypedRuleContext(BasicSQLGenParser.C_exprContext,0)


        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_having_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHaving_clause" ):
                listener.enterHaving_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHaving_clause" ):
                listener.exitHaving_clause(self)




    def having_clause(self):

        localctx = BasicSQLGenParser.Having_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_having_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(BasicSQLGenParser.HAVING)
            self.state = 144
            self.c_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sort_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDER(self):
            return self.getToken(BasicSQLGenParser.ORDER, 0)

        def BY(self):
            return self.getToken(BasicSQLGenParser.BY, 0)

        def sortby_list(self):
            return self.getTypedRuleContext(BasicSQLGenParser.Sortby_listContext,0)


        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_sort_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSort_clause" ):
                listener.enterSort_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSort_clause" ):
                listener.exitSort_clause(self)




    def sort_clause(self):

        localctx = BasicSQLGenParser.Sort_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_sort_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(BasicSQLGenParser.ORDER)
            self.state = 147
            self.match(BasicSQLGenParser.BY)
            self.state = 148
            self.sortby_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(BasicSQLGenParser.STAR, 0)

        def columnref(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicSQLGenParser.ColumnrefContext)
            else:
                return self.getTypedRuleContext(BasicSQLGenParser.ColumnrefContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BasicSQLGenParser.COMMA)
            else:
                return self.getToken(BasicSQLGenParser.COMMA, i)

        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_column_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_list" ):
                listener.enterColumn_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_list" ):
                listener.exitColumn_list(self)




    def column_list(self):

        localctx = BasicSQLGenParser.Column_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_column_list)
        self._la = 0 # Token type
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(BasicSQLGenParser.STAR)
                pass
            elif token in [634, 643, 656]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.columnref(0)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 152
                    self.match(BasicSQLGenParser.COMMA)
                    self.state = 153
                    self.columnref(0)
                    self.state = 158
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sortby_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sortby(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicSQLGenParser.SortbyContext)
            else:
                return self.getTypedRuleContext(BasicSQLGenParser.SortbyContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BasicSQLGenParser.COMMA)
            else:
                return self.getToken(BasicSQLGenParser.COMMA, i)

        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_sortby_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSortby_list" ):
                listener.enterSortby_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSortby_list" ):
                listener.exitSortby_list(self)




    def sortby_list(self):

        localctx = BasicSQLGenParser.Sortby_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_sortby_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.sortby()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 162
                self.match(BasicSQLGenParser.COMMA)
                self.state = 163
                self.sortby()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SortbyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnref(self):
            return self.getTypedRuleContext(BasicSQLGenParser.ColumnrefContext,0)


        def Identifier(self):
            return self.getToken(BasicSQLGenParser.Identifier, 0)

        def USING(self):
            return self.getToken(BasicSQLGenParser.USING, 0)

        def GT(self):
            return self.getToken(BasicSQLGenParser.GT, 0)

        def LT(self):
            return self.getToken(BasicSQLGenParser.LT, 0)

        def ASC(self):
            return self.getToken(BasicSQLGenParser.ASC, 0)

        def DESC(self):
            return self.getToken(BasicSQLGenParser.DESC, 0)

        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_sortby

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSortby" ):
                listener.enterSortby(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSortby" ):
                listener.exitSortby(self)




    def sortby(self):

        localctx = BasicSQLGenParser.SortbyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sortby)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.columnref(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(BasicSQLGenParser.Identifier)
                self.state = 171
                self.match(BasicSQLGenParser.USING)
                self.state = 172
                self.match(BasicSQLGenParser.GT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.match(BasicSQLGenParser.Identifier)
                self.state = 174
                self.match(BasicSQLGenParser.USING)
                self.state = 175
                self.match(BasicSQLGenParser.LT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 176
                self.match(BasicSQLGenParser.Identifier)
                self.state = 177
                self.match(BasicSQLGenParser.ASC)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 178
                self.match(BasicSQLGenParser.Identifier)
                self.state = 179
                self.match(BasicSQLGenParser.DESC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CollabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(BasicSQLGenParser.Identifier, 0)

        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_collabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCollabel" ):
                listener.enterCollabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCollabel" ):
                listener.exitCollabel(self)




    def collabel(self):

        localctx = BasicSQLGenParser.CollabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_collabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(BasicSQLGenParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Binary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(BasicSQLGenParser.AND, 0)

        def OR(self):
            return self.getToken(BasicSQLGenParser.OR, 0)

        def LT(self):
            return self.getToken(BasicSQLGenParser.LT, 0)

        def GT(self):
            return self.getToken(BasicSQLGenParser.GT, 0)

        def EQUAL(self):
            return self.getToken(BasicSQLGenParser.EQUAL, 0)

        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_binary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_op" ):
                listener.enterBinary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_op" ):
                listener.exitBinary_op(self)




    def binary_op(self):

        localctx = BasicSQLGenParser.Binary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_binary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8590132224) != 0) or _la==82):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BasicSQLGenParser.NOT, 0)

        def getRuleIndex(self):
            return BasicSQLGenParser.RULE_unary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_op" ):
                listener.enterUnary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_op" ):
                listener.exitUnary_op(self)




    def unary_op(self):

        localctx = BasicSQLGenParser.Unary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_unary_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(BasicSQLGenParser.NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.columnref_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def columnref_sempred(self, localctx:ColumnrefContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




