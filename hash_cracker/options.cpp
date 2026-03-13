#include <iostream>
#include "options.h"


Options::Options(int argc, char * argv[]){
    parse(argc, argv);
}

Options::Options(){}

void Options::parse(int argc, char * argv[]){
    for (auto i{1}; i < argc; ++i)
    {
        // convert argv[i] to string
        std::string arg{ argv[i] };
        // if (arg...)
        if (arg == "--md5") {
            md5_ = true;
            continue;
        }
        else if (arg == "--sha-256") {
            sha_256_ = true;
            continue;
        }
        else if (arg == "--help") {
            help_ = true;
            continue;
        }
        else if (arg == "--verbose"){
            verbose_ = true;
            continue;
        }

        if (arg[0] == '-'){
            for (const auto& c: arg.substr(1)){
                switch (c)
                {
                case 'm':
                    md5_ = true;
                    break;
                case 's':
                    sha_256_ = true;
                    break;
                case 'h':
                    help_ = true;
                    break;
                case 'v':
                    verbose_ = true;
                default:
                    throw std::invalid_argument{"Invalid flag"};
                }
            }
        }
        else{
            hash_.push_back(arg);  
        }
    }
}

bool Options::help() const{
    return help_;
}

bool Options::md5() const{
    return md5_;
}

bool Options::sha_256() const{
    return sha_256_;
}

bool Options::verbose() const{
    return verbose_;
}

const std::vector<std::string>& Options::hash() const{
    return hash_;
}

void Options::print(std::ostream& out) const{
    out << *this;
}


