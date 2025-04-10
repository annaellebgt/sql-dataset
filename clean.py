
import os
from antlr4 import *
from generated.BasicSQLGenLexer import BasicSQLGenLexer
from generated.BasicSQLGenParser import BasicSQLGenParser
from generated.TPCHSQLGenLexer import TPCHSQLGenLexer
from generated.TPCHSQLGenParser import TPCHSQLGenParser

def clean_queries(folder_path, parser_cls, lexer_cls, output_path="basic.sql"):
    
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(folder_path):
            if filename.endswith(".sql"):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    query = infile.read()
                    # if is_valid_sql(query, parser_cls, lexer_cls):
                    cleaned_line = query.strip().replace("\n", " ")
                    outfile.write(cleaned_line + "\n")
                    # else:
                    #     print(f"Not valid sql {file_path}")

def is_valid_sql(query, parser_cls, lexer_cls):
    try:
        input_stream = InputStream(query)
        lexer = lexer_cls(input_stream)
        stream = CommonTokenStream(lexer)
        parser = parser_cls(stream)

        parser.removeErrorListeners()  # Remove default console error printing
        parser._syntaxErrors = 0  # Reset error count

        # You need to call the top-level rule of your grammar here
        # Replace 'sql_script' with the correct entry rule for your SQL grammar
        tree = parser.select_statement()

        return parser._syntaxErrors == 0
    except Exception as e:
        return False


# folder_path="new_queries/TPC-H/"
# clean_queries(folder_path,TPCHSQLGenParser,TPCHSQLGenLexer,"tpc_h_queries.sql")

folder_path="new_queries/Basic/"
clean_queries(folder_path,BasicSQLGenParser,BasicSQLGenLexer,"basic.sql")
