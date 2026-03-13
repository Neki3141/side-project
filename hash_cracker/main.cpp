#include <iostream>
// #include <cstring>
// #include <openssl/md5.h>
#include <stdexcept>
#include "options.h"
#include "hashes.h"

auto help_text = "Usage: my_wc [OPTION]... [FILE]...\n"
    "Count lines, words, characters, and bytes in files.\n\n"

    "Options:\n"
    "  -l, --lines           print the line count\n"
    "  -w, --words           print the word count\n"
    "  -m, --characters      print the character count\n"
    "  -c, --bytes           print the byte count\n"
    "  -L, --longest-line    print the length of the longest line\n"
    "  -h, --help            display this help and exit\n"
    "  -v, --version         output version information and exit\n\n"

    "If no FILE is given, read from standard input.\n"; 

// void md5(const std::string& input, unsigned char output[MD5_DIGEST_LENGTH]) {
//     MD5((unsigned char*)input.c_str(), input.size(), output);
// }

int main(int argc, char* argv[]){
    try{
      Options opts{argc, argv};

      if (opts.verbose()){
        // print parsed options
        opts.print(std::cout);
      }

      if (opts.help()){
        std::cout << help_text;
        return EXIT_SUCCESS;
      }
      
      if (opts.hash().empty()){
        std::cout << "No file names passed.\n";
        std::cout << "Try `wc --help` for more information.\n";
        return EXIT_FAILURE;
      }
    }
    catch (const std::exception& e){
      std::cerr << "Error: " << e.what() << "\n";
      return EXIT_FAILURE;
    }
}